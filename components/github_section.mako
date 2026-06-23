<%def name="render(github_links)">
<section class="card github-section">
    % for index, (label, href) in enumerate(github_links):
        <a href="${href}">${label}</a>
        % if index in {0, 1, 3}:
            <span class="pipe">|</span>
        % endif
    % endfor
</section>
</%def>
