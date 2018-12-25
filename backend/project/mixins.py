import bleach
# from bleach.linkifier import Linker

from django.conf import settings


# linker = Linker(callbacks=[
#     bleach.callbacks.nofollow,
#     bleach.callbacks.target_blank,
# ])


class HtmlFieldsMixin(object):
    def save(self, *args, **kwargs):
        for field in self.html_fields:
            if isinstance(field, tuple):
                field_ = field[0]
                allowed_tags = field[1]

            else:
                field_ = field
                allowed_tags = settings.HTML_ALLOWED_TAGS

            val = getattr(self, field_)

            if val:
                val_clean = bleach.clean(
                    val,
                    tags=allowed_tags
                )

                setattr(self, field_, val_clean)

        return super(HtmlFieldsMixin, self).save(*args, **kwargs)
