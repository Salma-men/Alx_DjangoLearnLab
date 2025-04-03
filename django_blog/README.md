## Blog Comment System

### Features
- Users can leave comments on blog posts.
- Only authenticated users can add comments.
- Comment authors can edit or delete their own comments.

### URL Routes
- `/post/<post_id>/comment/new/` → Add a comment
- `/comment/<comment_id>/edit/` → Edit a comment
- `/comment/<comment_id>/delete/` → Delete a comment

## Tagging and Search Features

- Users can add tags to posts.
- Clicking on a tag filters all posts with that tag.
- Users can search for posts by title, content, or tags.
- Implemented using `django-taggit` and Django's `Q` object.

### How to Use:
- Add tags separated by commas when creating a post.
- Use the search bar to look for posts.
- Click on a tag to see related posts.