import markdown
import os

def convert_markdown_to_html(input_file, output_file):
    try:
        with open(input_file, 'r') as md_file:
            md_text = md_file.read()
        
        html_text = markdown.markdown(md_text)
        
        with open(output_file, 'w') as html_file:
            html_file.write(html_text)
        print(f"Successfully converted {input_file} to {output_file}")
    
    except Exception as e:
        print(f"Error: {e}")

def main():
    print("Markdown to HTML Converter")
    
    input_file = input("Enter the input markdown file path: ")
    if not os.path.isfile(input_file):
        print("The file does not exist.")
        return

    output_file = input("Enter the output HTML file path (e.g., output.html): ")
    
    convert_markdown_to_html(input_file, output_file)

if __name__ == "__main__":
    main()
