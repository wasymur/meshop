__author__ = 'wasy'


from django.db import models
from django.utils import timezone
from django.db.models.query import QuerySet


__author__ = 'Ori'

STD_MODEL_FIELDS = ('id', 'CreateDate', 'UpdateDate', )


class StdModelQuerySet(QuerySet):

    def delete(self):
        assert self.query.can_filter(), "Cannot use 'limit' or 'offset' with delete."
        for obj in self.all():
            obj.delete()
        self._result_cache = None
    delete.alters_data = True


class StdModelManager(models.Manager):

    def get_queryset(self):
        return StdModelQuerySet(self.model, using=self._db).filter(Deleted=False)

    def all_with_deleted(self):
        return StdModelQuerySet(self.model, using=self._db)


class StdModel(models.Model):
    ID = models.AutoField(primary_key=True)
    CreateDate = models.DateTimeField(auto_now_add=True)  # manage create dates
    UpdateDate = models.DateTimeField(auto_now=True , null=True , blank = True)  # manage change dates
    DeleteDate = models.DateTimeField(null=True, blank=True)
    Deleted = models.BooleanField(default=False)

    class Meta:
        abstract = True

    objects = StdModelManager()

    def __unicode__(self):
        create_date = self.CreateDate.strftime('%x') if self.CreateDate is not None else ''
        update_date = self.UpdateDate.strftime('%x') if self.UpdateDate is not None else ''
        temp = u"{0} ( created at {1}, last update {2} ) ".format(self.__class__.__name__, create_date, update_date)
        return temp

    def update(self, **kwargs):
        for k, v in kwargs.iteritems():
            setattr(self, k, v)
        self.save()

    def delete(self):
        related_objs = [relation.get_accessor_name() for relation in self._meta.get_all_related_objects()]
        for objs_model in related_objs:
            objs = getattr(self, objs_model).all()
            for obj in objs:
                if not issubclass(obj.__class__, StdModel):
                    break
                obj.delete()
        self.DeleteDate = timezone.now()
        self.Deleted = True
        self.save()


def code2text(code, choices):
    """
    Translates code to text in a choices based field

    :param code:        code that matches the first column of a choices based model integer field
    :param choices:     the choices tuple of pairs ((int_code1,text1), (int_code2,text2), ...)
    :return:            the text that matches the code or None
    """
    try:
        text = [x for x in choices if x[0] == code][0][1]
    except:
        text = None
    return text


def text2code(text, choices):
    """
    Translates text to code in a choices based field

    :param text:        text that matches the second column of a choices based model integer field
    :param choices:     the choices tuple of pairs ((int_code1,text1), (int_code2,text2), ...)
    :return:            the code that matches the text or None
    """
    try:
        text = text.lower()
        code = [x for x in choices if x[1] == text][0][0]
    except:
        code = None
    return code
