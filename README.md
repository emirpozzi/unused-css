# Purge CSS CLI for Angular

Remove unused CSS and Sass classes from your Angular project.

Purge CSS for Angular finds unused CSS classes in your `.component.css` and `.component.scss` files.
It also checks if there unused classes in Sass partials and global stylesheets (`_foo.scss, index.css` etc.)

The CLI outputs a list of the unused CSS classes and it **does not** modify anyfile.

To run navigate to the Angular project `src` folder and run:

```
python3 <abs-path-to-script-folder>/purge_css.py
```

To find unused css outside component style files such as Sass partial files and index.css run:

```
python3 <abs-path-to-script-folder>/purge_modules.py
```
