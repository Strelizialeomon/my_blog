from django.contrib.syndication.views import Feed

from blog.models import Entry


class LastestEntriesFeed(Feed):
    title = "Lemon_vita的博客"
    link = "/siteblogs/"
    description = "Lemon_vita的最新博客"

    def items(self):
        return Entry.objects.order_by('-created_time')[:5]

    def item_title(self, item):
        return item.title

    def item_description(self, item):
        return item.abstract
