def define_env(env):
    @env.macro
    def class_all_options(class_name, separate_signature=True):
        return f"""
::: {class_name}
    options:
        show_root_toc_entry: true
        show_bases: true
        separate_signature: {str(separate_signature).lower()}
        extra:
            show_class_docstring: true
            show_children: true
        summary:
            attributes: true
            functions: true
"""

    @env.macro
    def class_summary(class_name, screenshot=None):
        control_name = class_name.split(".")[-1]
        screenshot_md = f"\n\n![{control_name}]({screenshot})\n\n" if screenshot else ""
        return f"""
::: {class_name}
    options:
        show_root_toc_entry: true
        extra:
            show_class_docstring: true

{screenshot_md}
        
::: {class_name}
    options:
        show_bases: true
        summary:
            attributes: true
            functions: true
"""

    @env.macro
    def class_members(class_name):
        return f"""
::: {class_name}
    options:
        extra:
            show_children: true
"""
