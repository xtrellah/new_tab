<!doctype html>
<%namespace name="github_section" file="components/github_section.mako" />\
<%namespace name="search_section" file="components/search_section.mako" />\
<%namespace name="links_section" file="components/links_section.mako" />\
<html lang="en">
    <head>
        <meta charset="UTF-8" />
        <meta name="viewport" content="width=device-width, initial-scale=1.0" />
        <title>New Tab</title>

        <link rel="stylesheet" href="styles/default.css" />
        <link rel="stylesheet" href="styles/steam.css" />
    </head>
    <body>
        <main class="container">
            % for component in components:
                % if component["type"] == "github_section":
                    ${github_section.render(component["config"])}
                % elif component["type"] == "search_bar":
                    ${search_section.render(component["config"])}
                % elif component["type"] == "card_section":
                    ${links_section.render(component["config"])}
                % endif
            % endfor
        </main>
        <script>
            window.addEventListener("load", () => {
                document.querySelector(".search-input")?.focus();
            });
        </script>
    </body>
</html>
