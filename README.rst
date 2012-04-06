Move Fitness website
====================


How it works
------------

The main app in the project is the `content` app. It has just one model, with 3 fields:
 - title
 - description
 - slug

This model aims to reflect the content of the pages present in the website. Each page has a title and a description,
except for the index page.

Template renderization process
------------------------------

Pages also have some other kind of content, like a galery, or a map, that's why we don't render all content records with one
single template, then we can easily differ from one content to another in the template layer.
The renderization process searchs for the record's slug. For example, if you have a content recorded with the following fields:

 - title: Activities
 - description: This is a description
 - slug: activities

Then, when the `domain.com/activities` is called, the view will search for a template named `activities.html` inside
`content/templates` directory. It means that whenever you create a new content record, all you need to do to create a new
page for it is create a new template and inherit from the `base.html` template.
