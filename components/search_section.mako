<%def name="render()">
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
</%def>
