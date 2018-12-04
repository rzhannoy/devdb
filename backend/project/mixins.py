import bleach
from bleach.linkifier import Linker

from django.conf import settings


linker = Linker(callbacks=[
    bleach.callbacks.nofollow,
    bleach.callbacks.target_blank,
])


class HtmlFieldsMixin(object):
    def save(self, *args, **kwargs):
        for field in self.html_fields:
            val = getattr(self, field)

            if val:
                val_clean = bleach.clean(
                    val,
                    tags=settings.HTML_ALLOWED_TAGS
                )
                # val_clean = linker.linkify(val_clean)

                setattr(self, field, val_clean)

        return super(HtmlFieldsMixin, self).save(*args, **kwargs)
