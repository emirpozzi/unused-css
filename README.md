# Purge CSS CLI for Angular

Remove unused CSS and Sass classes from your Angular project.

Purge CSS for Angular finds unused CSS classes in your `.component.css` and `.component.scss` files.
It also checks if there are unused classes in Sass partials and global stylesheets (`_foo.scss, index.css` etc.)

The CLI outputs a list of the unused CSS classes and it **DOES NOT** modify anyfile.

To run navigate to an Angular project `src` folder and run:

```
python3 <abs-path-to-script-folder>/purge_css.py
```
