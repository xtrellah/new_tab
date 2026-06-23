<%def name="render(section)">
<section class="card links-section">
    <h2>${section["title"]}</h2>

    <div class="link-grid">
        % for item in section["items"]:
            <a class="link-card" href="${item["href"]}">${item["label"]}</a>
        % endfor
    </div>
</section>
</%def>
