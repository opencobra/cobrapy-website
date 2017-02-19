# The new Cobrapy website

This is a basic mockup for the new cobrapy website. It uses a lighter design follwoing the the Material Design spec and provides ther basic section:

- general info
- packages using cobrapy
- publications using cobrapy

## Dev setup

The site itself is build with [Hugo](http://gohugo.io). Please see the [Hugo Docs](http://gohugo.io/overview/introduction/) for a general introduction.

### Installing Hugo

Hugo is a single binary that can be downloaded for a large set of platforms from the [hugo releases page](https://github.com/spf13/hugo/releases). On Mac you can also use homebrew via `brew install hugo`. For further instructions see the [Hugo installation instruction](http://gohugo.io/overview/installing/).

### Editing the site

After installing hugo clone the website source with

```bash
git clone https://github.com/opencobra/cobrapy-website
```

You can start the live web server with

```
cd cobrapy_website
hugo server
```

This will serve the website on http://localhost:1313/cobrapy and will rebuild the site automaticaly everytime you change any of the files.

The actual Markdown content can be found in the `content` folder. `intro` are the sections shown on the Homepage, `packages` are the software packages using cobrapy and `pubs` are the publications (automatically generated using the `pubmed_to_hugo.py` script from a Pubmed XML).

Templates and logic are contained in the `layouts` folder as detailed in the Hugo Docs.
