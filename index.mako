<!doctype html>
<%namespace name="github_section" file="components/github_section.mako" />\
<%namespace name="search_section" file="components/search_section.mako" />\
<%namespace name="links_section" file="components/links_section.mako" />\
<html lang="en">
    <head>
        <meta charset="UTF-8" />
        <meta name="viewport" content="width=device-width, initial-scale=1.0" />
        <title>New Tab</title>

        <link rel="stylesheet" href="styles/matrix.css" />
    </head>
    <body>
        <main class="container">

            ${github_section.render(github_links)}

            ${search_section.render()}

            ${links_section.render(link_cards)}

        </main>
        <script>
            window.addEventListener("load", () => {
                document.querySelector(".search-input")?.focus();
            });
        </script>
    </body>
</html>
