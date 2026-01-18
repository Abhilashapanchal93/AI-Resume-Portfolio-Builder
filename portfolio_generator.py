from jinja2 import Template

def generate_portfolio(data, theme="modern", output_file="portfolio.html"):
    template_path = f"portfolio_templates/{theme}.html"

    with open(template_path, "r", encoding="utf-8") as f:
        template = Template(f.read())

    html = template.render(**data)

    with open(output_file, "w", encoding="utf-8") as f:
        f.write(html)

    return output_file
