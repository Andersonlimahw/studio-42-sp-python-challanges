import sys

# Import settings from settings.py
from settings import name

def render_template(template_file, output_file):
    try:
        # Read the template file
        with open(template_file, 'r') as template:
            template_content = template.read()

        # Replace the {name} placeholder with the value from settings
        template_content = template_content.replace("{name}", name)

        # Write the result to an HTML file
        with open(output_file, 'w') as output:
            output.write(template_content)

        print(f"Template rendered successfully to {output_file}")

    except FileNotFoundError:
        print(f"Error: {template_file} not found.")
    except Exception as e:
        print(f"An error occurred: {str(e)}")

if __name__ == '__main__':
    if len(sys.argv) != 2:
        print("Usage: render.py input_template_file.template")
        sys.exit(1)

    input_template_file = sys.argv[1]
    output_file = input_template_file.replace(".template", ".html")

    render_template(input_template_file, output_file)
