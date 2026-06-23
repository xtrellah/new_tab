<%def name="render(search_bar)">
<section class="search-section">
    <form action="${search_bar["action"]}" method="${search_bar["method"]}">
        <input
            type="text"
            name="${search_bar["name"]}"
            class="search-input"
            placeholder="${search_bar["placeholder"]}"
            autocomplete="${search_bar["autocomplete"]}"
            % if search_bar["autofocus"]:
                autofocus
            % endif
            % if search_bar["required"]:
                required
            % endif
        />
    </form>
</section>
</%def>
