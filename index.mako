<!doctype html>
<html lang="en">
    <head>
        <meta charset="UTF-8" />
        <meta name="viewport" content="width=device-width, initial-scale=1.0" />
        <title>New Tab</title>

        <link rel="stylesheet" href="styles/matrix.css" />
        <!--<link rel="stylesheet" href="styles/retroma.css" />-->
        <!--<link rel="stylesheet" href="styles/steam.css" />-->
        <!--<link rel="stylesheet" href="styles/neo-brutalist.css" />-->
    </head>
    <body>
        <main class="container">

            <!-- TOP BAR -->
            <section class="card github-section">
                % for index, (label, href) in enumerate(github_links):
                    <a href="${href}">${label}</a>
                    % if index in {0, 2, 3}:
                        <span class="pipe">|</span>
                    % endif
                % endfor
            </section>

            <!-- SEARCH BAR -->
            <section class="search-section">
                <form action="https://www.google.com/search" method="GET">
                    <input
                        type="text"
                        name="q"
                        class="search-input"
                        placeholder="Search (googoo)"
                        autocomplete="off"
                        autofocus
                        required
                    />
                </form>
            </section>

            <!-- LINK GRID -->
            <section class="card links-section">
                <h2>Links</h2>

                <div class="link-grid">
                    % for label, href in link_cards:
                        <a class="link-card" href="${href}">${label}</a>
                    % endfor
                </div>
            </section>

        </main>
        <script>
            window.addEventListener("load", () => {
                document.querySelector(".search-input")?.focus();
            });
        </script>
    </body>
</html>
