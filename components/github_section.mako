<%def name="render(section)">
<section class="card github-section">
    % for item in section["items"]:
        % if item["type"] == "pipe":
            <span class="pipe">|</span>
        % else:
            <a href="${item["href"]}">${item["label"]}</a>
        % endif
    % endfor
</section>
</%def>
