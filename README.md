# Northstar Advisory Business Landing Page

Northstar Advisory is a two-page business landing website built with semantic HTML and CSS for the Udacity Front End Web Developer Nanodegree. The project is structured as a lightweight static site with a polished visual system, responsive layouts, and clear page-level organization that maps directly to the project rubric.

## Project Overview

The site presents a fictional consulting firm and includes:

- A home page with a navigation bar, hero banner, service cards, about content, supporting imagery, testimonial content, and footer
- A secondary contact page with contact information, a structured inquiry form, and supporting FAQ content
- Separate global and page-specific stylesheets to keep shared styling and page-level rules maintainable
- Responsive layouts that adapt cleanly across mobile, tablet, and desktop viewports

## File Structure

```text
.
|-- index.html
|-- css/
|   |-- contact.css
|   |-- global.css
|   `-- home.css
|-- images/
|   |-- meeting-room.jpg
|   `-- team-collaboration.jpg
`-- pages/
    `-- contact/
        `-- index.html
```

## Design Notes

This implementation uses a restrained editorial style to keep the project submission-ready while still feeling portfolio quality:

- A navy and amber color palette creates contrast without relying on generic dark-mode styling
- Fraunces is used for headings and DM Sans is used for interface and paragraph text to create clearer typographic hierarchy
- CSS Grid powers the service-card and contact-detail layouts, while Flexbox handles navigation, button groups, and footer alignment
- The layout stays intentionally lightweight so the focus remains on semantic structure, readability, and responsiveness

## Setup and Usage

No build tools or package installation are required.

1. Clone the repository.
2. Open `index.html` directly in a browser, or serve the repository root with a local static server.

Example using Python:

```bash
python -m http.server 8000
```

Then visit `http://localhost:8000`.

## Testing and Verification

Because this is a static HTML/CSS project, validation is primarily structural and visual:

- Checked the page structure against the project rubric requirements
- Verified that the site uses separate global and page-level CSS files
- Confirmed both pages link correctly through the shared navigation
- Reviewed responsiveness at mobile, tablet, and desktop viewport widths
- Confirmed the form includes labels, validation-friendly input types, and required fields

Run the lightweight structural checks with:

```bash
python -m unittest discover -s tests
```

## Image Credits

The project replaces the provided stock photos with free Unsplash images:

- `images/team-collaboration.jpg` by Campaign Creators: <https://unsplash.com/photos/people-sitting-near-table-with-laptop-computer-qCi_MzVODoU>
- `images/meeting-room.jpg` by Marc Wieland: <https://unsplash.com/photos/modern-meeting-room-with-city-view-yzOieLQof-U>

## Tradeoffs and Limitations

- The contact form is a front-end-only form and does not submit to a live backend service
- The project uses externally hosted Google Fonts for typography, so the custom typefaces depend on network availability
- Automated test coverage is intentionally minimal because the project scope is static HTML and CSS rather than application logic
