
import markdown

txt="[[type='checkbox' value=\"1\"]]"

md = markdown.markdown(txt, extensions=["md_inputs"])

print(md)
