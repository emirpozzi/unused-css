# UnusedCSS for Angular

Remove unused CSS and Sass classes from an Angular project.

UnusedCSS for Angular finds unused CSS classes in your ".component.css" and ".component.scss" files.
It also checks if there are unused classes in Sass partials and global stylesheets ("\_foo.scss", "index.css" etc.)

The CLI outputs a list of the unused CSS classes and it **DOES NOT** modify anyfile.

To run navigate to an Angular project src folder and run:

```
python3 purge_css.py
```

Or pass the project src folder absolute path as an argument:

```
python3 purge_css.py /Users/me/project/src
```
