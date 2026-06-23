<%def name="render(link_cards)">
<section class="card links-section">
    <h2>Links</h2>

    <div class="link-grid">
        % for label, href in link_cards:
            <a class="link-card" href="${href}">${label}</a>
        % endfor
    </div>
</section>
</%def>
