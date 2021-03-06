# coding: utf-8
from django.utils.translation import gettext_lazy as _
from django.db import models

from common.constants import BIGVS_DA_V_TYPE_CHOICES, BIGVS_IS_DEFAULT_CHOICES


class BigVs(models.Model):
    v_id = models.CharField(_(u'id'), max_length=36, unique=True)
    name = models.CharField(_(u'名称'), max_length=32, blank=True, null=True)
    da_v_type = models.IntegerField(_(u'类型'), blank=True, null=True, choices=BIGVS_DA_V_TYPE_CHOICES)
    belong_to = models.IntegerField(_(u'机构'), blank=True, null=True)
    synonym = models.TextField(_(u'同义词'), blank=True, null=True)
    pinyin = models.CharField(_(u'拼音'), max_length=256, blank=True, null=True)
    isdefault = models.IntegerField(_(u'名称类型'), blank=True, null=True, choices=BIGVS_IS_DEFAULT_CHOICES)
    words_weight = models.IntegerField(_(u'言值'), blank=True, null=True)
    brief = models.TextField(_(u'概要'), blank=True, null=True)
    introduction = models.TextField(_(u'简介'), blank=True, null=True)
    headimg = models.ImageField(_(u'头像'), blank=True, null=True, upload_to='bigv')
    initials = models.CharField(_(u'首字母'), max_length=64, blank=True, null=True)
 
    class Meta:
        managed = False
        db_table = 'big_vs'
        verbose_name = verbose_name_plural = _(u'大V')
        ordering = ('-words_weight',)
    
    def __unicode__(self):
        return self.name
        
class BigVsSrc(models.Model):
    v_id = models.CharField(_(u'vid'), max_length=36)
    name = models.CharField(_(u'名称'), max_length=64)
    nickname = models.CharField(_(u'昵称'), max_length=64, blank=True, null=True)
    category = models.CharField(_(u'分类'), max_length=36, blank=True, null=True)
    gender = models.CharField(_(u'性别'), max_length=6, blank=True, null=True)
    brief = models.TextField(_(u'简介'), blank=True, null=True)
    url = models.CharField(_(u'主页'), max_length=256, blank=True, null=True)
    fans_count = models.IntegerField(_(u'粉丝数'), blank=True, null=True)
    follows_count = models.IntegerField(_(u'关注数'), blank=True, null=True)
    content_count = models.IntegerField(_(u'评论数'), blank=True, null=True)
    words_weight = models.IntegerField(_(u'言值'), blank=True, null=True)
    related_weight = models.IntegerField(_(u'相关度'), blank=True, null=True)
    comment = models.TextField(_(u'备注'), blank=True, null=True)
 
    class Meta:
        managed = False
        db_table = 'big_vs_src'
        verbose_name = verbose_name_plural = _(u'大V')
        
    def __unicode__(self):
        return '{0}--{1}'.format(self.name, self.category)
