import re
import unittest
from html.parser import HTMLParser
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]


class PageParser(HTMLParser):
    def __init__(self):
        super().__init__()
        self.h1_count = 0
        self.stylesheets = []
        self.images = []
        self.labels = []
        self.controls = []
        self.has_form = False
        self.links = []

    def handle_starttag(self, tag, attrs):
        attributes = dict(attrs)

        if tag == "h1":
            self.h1_count += 1

        if tag == "link" and attributes.get("rel") == "stylesheet":
            self.stylesheets.append(attributes.get("href"))

        if tag == "img":
            self.images.append(attributes.get("alt", ""))

        if tag == "label":
            self.labels.append(attributes.get("for"))

        if tag in {"input", "textarea"}:
            self.controls.append(attributes.get("id"))

        if tag == "form":
            self.has_form = True

        if tag == "a":
            self.links.append(attributes.get("href"))


def parse_page(path):
    parser = PageParser()
    parser.feed(path.read_text(encoding="utf-8"))
    return parser


class StructureTests(unittest.TestCase):
    def test_required_files_exist(self):
        required_paths = [
            ROOT / "index.html",
            ROOT / "pages" / "contact" / "index.html",
            ROOT / "css" / "global.css",
            ROOT / "css" / "home.css",
            ROOT / "css" / "contact.css",
            ROOT / "images" / "team-collaboration.jpg",
            ROOT / "images" / "meeting-room.jpg",
            ROOT / "README.md",
        ]

        for path in required_paths:
            with self.subTest(path=path):
                self.assertTrue(path.exists())

    def test_home_page_semantics(self):
        parser = parse_page(ROOT / "index.html")

        self.assertEqual(parser.h1_count, 1)
        self.assertGreaterEqual(len(parser.stylesheets), 2)
        self.assertGreaterEqual(len(parser.images), 2)
        self.assertTrue(all(alt.strip() for alt in parser.images))
        self.assertIn("pages/contact/index.html", parser.links)

    def test_contact_page_semantics(self):
        parser = parse_page(ROOT / "pages" / "contact" / "index.html")

        self.assertEqual(parser.h1_count, 1)
        self.assertGreaterEqual(len(parser.stylesheets), 2)
        self.assertTrue(parser.has_form)
        self.assertTrue(all(control in parser.labels for control in parser.controls))
        self.assertIn("../../index.html", parser.links)

    def test_css_includes_required_layout_features(self):
        global_css = (ROOT / "css" / "global.css").read_text(encoding="utf-8")
        home_css = (ROOT / "css" / "home.css").read_text(encoding="utf-8")
        contact_css = (ROOT / "css" / "contact.css").read_text(encoding="utf-8")
        combined_css = "\n".join([global_css, home_css, contact_css])

        self.assertIn("display: flex", combined_css)
        self.assertIn("display: grid", combined_css)
        self.assertIn("@media", combined_css)
        self.assertRegex(combined_css, re.compile(r"#[0-9a-fA-F]{3,6}"))


if __name__ == "__main__":
    unittest.main()
