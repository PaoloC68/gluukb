# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'QuestionReference'
        db.create_table(u'sugarlink_questionreference', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('case', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['sugarmodels.Case'])),
            ('question', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['knowledge.Question'])),
        ))
        db.send_create_signal(u'sugarlink', ['QuestionReference'])


    def backwards(self, orm):
        # Deleting model 'QuestionReference'
        db.delete_table(u'sugarlink_questionreference')


    models = {
        u'auth.group': {
            'Meta': {'object_name': 'Group'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '80'}),
            'permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'})
        },
        u'auth.permission': {
            'Meta': {'ordering': "(u'content_type__app_label', u'content_type__model', u'codename')", 'unique_together': "((u'content_type', u'codename'),)", 'object_name': 'Permission'},
            'codename': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['contenttypes.ContentType']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        u'auth.user': {
            'Meta': {'object_name': 'User'},
            'date_joined': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'blank': 'True'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'groups': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['auth.Group']", 'symmetrical': 'False', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'is_staff': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_superuser': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'last_login': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'user_permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'}),
            'username': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '30'})
        },
        u'contenttypes.contenttype': {
            'Meta': {'ordering': "('name',)", 'unique_together': "(('app_label', 'model'),)", 'object_name': 'ContentType', 'db_table': "'django_content_type'"},
            'app_label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        u'knowledge.category': {
            'Meta': {'ordering': "['title']", 'object_name': 'Category'},
            'added': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'lastchanged': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'slug': ('django.db.models.fields.SlugField', [], {'unique': 'True', 'max_length': '50'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        },
        u'knowledge.question': {
            'Meta': {'ordering': "['-added']", 'object_name': 'Question'},
            'added': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'alert': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'body': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'categories': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['knowledge.Category']", 'symmetrical': 'False', 'blank': 'True'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'lastchanged': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'locked': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '64', 'null': 'True', 'blank': 'True'}),
            'status': ('django.db.models.fields.CharField', [], {'default': "'private'", 'max_length': '32', 'db_index': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['auth.User']", 'null': 'True', 'blank': 'True'})
        },
        u'sugarlink.questionreference': {
            'Meta': {'object_name': 'QuestionReference'},
            'case': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['sugarmodels.Case']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'question': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['knowledge.Question']"})
        },
        u'sugarmodels.account': {
            'Meta': {'object_name': 'Account', 'db_table': "u'accounts'", 'managed': 'False'},
            'account_type': ('django.db.models.fields.CharField', [], {'max_length': '50L', 'blank': 'True'}),
            'annual_revenue': ('django.db.models.fields.CharField', [], {'max_length': '100L', 'blank': 'True'}),
            'assigned_user': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "u'accounts_assigned'", 'null': 'True', 'db_column': "u'assigned_user_id'", 'to': u"orm['sugarmodels.SugarUser']"}),
            'billing_address_city': ('django.db.models.fields.CharField', [], {'max_length': '100L', 'blank': 'True'}),
            'billing_address_country': ('django.db.models.fields.CharField', [], {'max_length': '255L', 'blank': 'True'}),
            'billing_address_postalcode': ('django.db.models.fields.CharField', [], {'max_length': '20L', 'blank': 'True'}),
            'billing_address_state': ('django.db.models.fields.CharField', [], {'max_length': '100L', 'blank': 'True'}),
            'billing_address_street': ('django.db.models.fields.CharField', [], {'max_length': '150L', 'blank': 'True'}),
            'contacts': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['sugarmodels.Contact']", 'through': u"orm['sugarmodels.AccountContact']", 'symmetrical': 'False'}),
            'created_by': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "u'account_created_by_user'", 'null': 'True', 'db_column': "u'created_by'", 'to': u"orm['sugarmodels.SugarUser']"}),
            'date_entered': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'date_modified': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'deleted': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'description': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'emails': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['sugarmodels.EmailAddress']", 'through': u"orm['sugarmodels.EmailAccount']", 'symmetrical': 'False'}),
            'employees': ('django.db.models.fields.CharField', [], {'max_length': '10L', 'blank': 'True'}),
            'id': ('django_uuid.fields.UUIDField', [], {'max_length': '36', 'primary_key': 'True'}),
            'industry': ('django.db.models.fields.CharField', [], {'max_length': '50L', 'blank': 'True'}),
            'modified_by_user': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "u'accounts_modified'", 'null': 'True', 'db_column': "u'modified_user_id'", 'to': u"orm['sugarmodels.SugarUser']"}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '150L', 'blank': 'True'}),
            'ownership': ('django.db.models.fields.CharField', [], {'max_length': '100L', 'blank': 'True'}),
            'parent_id': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['sugarmodels.Account']", 'null': 'True', 'db_column': "u'parent_id'", 'blank': 'True'}),
            'phone_alternate': ('django.db.models.fields.CharField', [], {'max_length': '100L', 'blank': 'True'}),
            'phone_fax': ('django.db.models.fields.CharField', [], {'max_length': '100L', 'blank': 'True'}),
            'phone_office': ('django.db.models.fields.CharField', [], {'max_length': '100L', 'blank': 'True'}),
            'rating': ('django.db.models.fields.CharField', [], {'max_length': '100L', 'blank': 'True'}),
            'shipping_address_city': ('django.db.models.fields.CharField', [], {'max_length': '100L', 'blank': 'True'}),
            'shipping_address_country': ('django.db.models.fields.CharField', [], {'max_length': '255L', 'blank': 'True'}),
            'shipping_address_postalcode': ('django.db.models.fields.CharField', [], {'max_length': '20L', 'blank': 'True'}),
            'shipping_address_state': ('django.db.models.fields.CharField', [], {'max_length': '100L', 'blank': 'True'}),
            'shipping_address_street': ('django.db.models.fields.CharField', [], {'max_length': '150L', 'blank': 'True'}),
            'sic_code': ('django.db.models.fields.CharField', [], {'max_length': '10L', 'blank': 'True'}),
            'ticker_symbol': ('django.db.models.fields.CharField', [], {'max_length': '10L', 'blank': 'True'}),
            'website': ('django.db.models.fields.CharField', [], {'max_length': '255L', 'blank': 'True'})
        },
        u'sugarmodels.accountcontact': {
            'Meta': {'object_name': 'AccountContact', 'db_table': "u'accounts_contacts'", 'managed': 'False'},
            'account': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['sugarmodels.Account']", 'db_column': "u'account_id'"}),
            'contact': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['sugarmodels.Contact']", 'db_column': "u'contact_id'"}),
            'date_modified': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'deleted': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'id': ('django_uuid.fields.UUIDField', [], {'max_length': '36', 'primary_key': 'True'})
        },
        u'sugarmodels.case': {
            'Meta': {'object_name': 'Case', 'db_table': "u'cases'", 'managed': 'False'},
            'account': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['sugarmodels.Account']", 'null': 'True', 'db_column': "u'account_id'"}),
            'assigned_user': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "u'cases_assigned'", 'null': 'True', 'db_column': "u'assigned_user_id'", 'to': u"orm['sugarmodels.SugarUser']"}),
            'case_number': ('django.db.models.fields.IntegerField', [], {'null': 'True'}),
            'contacts': ('django.db.models.fields.related.ManyToManyField', [], {'related_name': "u'cases'", 'symmetrical': 'False', 'through': u"orm['sugarmodels.ContactCase']", 'to': u"orm['sugarmodels.Contact']"}),
            'created_by': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "u'cases_created'", 'null': 'True', 'db_column': "u'created_by'", 'to': u"orm['sugarmodels.SugarUser']"}),
            'date_entered': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'date_modified': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'deleted': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'description': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'id': ('django_uuid.fields.UUIDField', [], {'max_length': '36', 'primary_key': 'True'}),
            'modified_by_user': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "u'cases_modified'", 'null': 'True', 'db_column': "u'modified_user_id'", 'to': u"orm['sugarmodels.SugarUser']"}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255L', 'null': 'True', 'blank': 'True'}),
            'priority': ('django.db.models.fields.CharField', [], {'default': "u'P1'", 'max_length': '100L', 'null': 'True'}),
            'resolution': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'status': ('django.db.models.fields.CharField', [], {'default': "u'New'", 'max_length': '100L', 'null': 'True'}),
            'type': ('django.db.models.fields.CharField', [], {'default': "u'Administration'", 'max_length': '255L', 'null': 'True', 'blank': 'True'}),
            'work_log': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'})
        },
        u'sugarmodels.contact': {
            'Meta': {'object_name': 'Contact', 'db_table': "u'contacts'", 'managed': 'False'},
            'alt_address_city': ('django.db.models.fields.CharField', [], {'max_length': '100L', 'blank': 'True'}),
            'alt_address_country': ('django.db.models.fields.CharField', [], {'max_length': '255L', 'blank': 'True'}),
            'alt_address_postalcode': ('django.db.models.fields.CharField', [], {'max_length': '20L', 'blank': 'True'}),
            'alt_address_state': ('django.db.models.fields.CharField', [], {'max_length': '100L', 'blank': 'True'}),
            'alt_address_street': ('django.db.models.fields.CharField', [], {'max_length': '150L', 'blank': 'True'}),
            'assigned_user': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "u'contacts_assigned'", 'null': 'True', 'to': u"orm['sugarmodels.SugarUser']"}),
            'assistant': ('django.db.models.fields.CharField', [], {'max_length': '75L', 'blank': 'True'}),
            'assistant_phone': ('django.db.models.fields.CharField', [], {'max_length': '100L', 'blank': 'True'}),
            'birthdate': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'created_by': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "u'contacts_created'", 'null': 'True', 'db_column': "u'created_by'", 'to': u"orm['sugarmodels.SugarUser']"}),
            'date_entered': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'date_modified': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'deleted': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'department': ('django.db.models.fields.CharField', [], {'max_length': '255L', 'blank': 'True'}),
            'description': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'do_not_call': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'emails': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['sugarmodels.EmailAddress']", 'through': u"orm['sugarmodels.EmailContact']", 'symmetrical': 'False'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '100L', 'blank': 'True'}),
            'id': ('django_uuid.fields.UUIDField', [], {'max_length': '36', 'primary_key': 'True'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '100L', 'blank': 'True'}),
            'lead_source': ('django.db.models.fields.CharField', [], {'max_length': '255L', 'blank': 'True'}),
            'modified_by_user': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "u'contacts_modified'", 'null': 'True', 'db_column': "u'modified_user_id'", 'to': u"orm['sugarmodels.SugarUser']"}),
            'phone_fax': ('django.db.models.fields.CharField', [], {'max_length': '100L', 'blank': 'True'}),
            'phone_home': ('django.db.models.fields.CharField', [], {'max_length': '100L', 'blank': 'True'}),
            'phone_mobile': ('django.db.models.fields.CharField', [], {'max_length': '100L', 'blank': 'True'}),
            'phone_other': ('django.db.models.fields.CharField', [], {'max_length': '100L', 'blank': 'True'}),
            'phone_work': ('django.db.models.fields.CharField', [], {'max_length': '100L', 'blank': 'True'}),
            'portal_active': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'portal_app': ('django.db.models.fields.CharField', [], {'max_length': '255L', 'blank': 'True'}),
            'portal_name': ('django.db.models.fields.CharField', [], {'max_length': '255L', 'blank': 'True'}),
            'primary_address_city': ('django.db.models.fields.CharField', [], {'max_length': '100L', 'blank': 'True'}),
            'primary_address_country': ('django.db.models.fields.CharField', [], {'max_length': '255L', 'blank': 'True'}),
            'primary_address_postalcode': ('django.db.models.fields.CharField', [], {'max_length': '20L', 'blank': 'True'}),
            'primary_address_state': ('django.db.models.fields.CharField', [], {'max_length': '100L', 'blank': 'True'}),
            'primary_address_street': ('django.db.models.fields.CharField', [], {'max_length': '150L', 'blank': 'True'}),
            'reports_to': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['sugarmodels.Contact']", 'null': 'True', 'db_column': "u'reports_to_id'", 'blank': 'True'}),
            'salutation': ('django.db.models.fields.CharField', [], {'max_length': '255L', 'blank': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '100L', 'blank': 'True'})
        },
        u'sugarmodels.contactcase': {
            'Meta': {'object_name': 'ContactCase', 'db_table': "u'contacts_cases'", 'managed': 'False'},
            'case': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['sugarmodels.Case']", 'db_column': "u'case_id'"}),
            'contact': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['sugarmodels.Contact']", 'db_column': "u'contact_id'"}),
            'contact_role': ('django.db.models.fields.CharField', [], {'max_length': '50L', 'null': 'True', 'blank': 'True'}),
            'date_modified': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'deleted': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'id': ('django_uuid.fields.UUIDField', [], {'max_length': '36', 'primary_key': 'True'})
        },
        u'sugarmodels.emailaccount': {
            'Meta': {'object_name': 'EmailAccount', 'db_table': "u'email_addr_bean_rel'", 'managed': 'False'},
            'account': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "u'emails_of_account'", 'null': 'True', 'db_column': "u'bean_id'", 'to': u"orm['sugarmodels.Account']"}),
            'bean_module': ('django.db.models.fields.CharField', [], {'default': "u'Accounts'", 'max_length': '100L', 'blank': 'True'}),
            'date_created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'date_modified': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'deleted': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'email_accounts_id': ('django_uuid.fields.UUIDField', [], {'max_length': '36', 'primary_key': 'True', 'db_column': "u'id'"}),
            'email_address': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "u'accounts_of_email'", 'db_column': "u'email_address_id'", 'to': u"orm['sugarmodels.EmailAddress']"}),
            'primary_address': ('django.db.models.fields.IntegerField', [], {'default': '1', 'null': 'True', 'blank': 'True'}),
            'reply_to_address': ('django.db.models.fields.IntegerField', [], {'default': '0', 'null': 'True', 'blank': 'True'})
        },
        u'sugarmodels.emailaddress': {
            'Meta': {'object_name': 'EmailAddress', 'db_table': "u'email_addresses'", 'managed': 'False'},
            'date_created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'date_modified': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'deleted': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'email_address': ('django.db.models.fields.CharField', [], {'max_length': '255L', 'blank': 'True'}),
            'email_address_caps': ('django.db.models.fields.CharField', [], {'max_length': '255L', 'blank': 'True'}),
            'email_id': ('django_uuid.fields.UUIDField', [], {'max_length': '36', 'primary_key': 'True', 'db_column': "u'id'"}),
            'invalid_email': ('django.db.models.fields.IntegerField', [], {'default': '0', 'null': 'True', 'blank': 'True'}),
            'opt_out': ('django.db.models.fields.IntegerField', [], {'default': '0', 'null': 'True', 'blank': 'True'})
        },
        u'sugarmodels.emailcontact': {
            'Meta': {'object_name': 'EmailContact', 'db_table': "u'email_addr_bean_rel'", 'managed': 'False'},
            'account': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "u'email_of_contact'", 'null': 'True', 'db_column': "u'bean_id'", 'to': u"orm['sugarmodels.Contact']"}),
            'bean_module': ('django.db.models.fields.CharField', [], {'default': "u'Contacts'", 'max_length': '100L', 'blank': 'True'}),
            'date_created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'date_modified': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'deleted': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'email_address': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "u'contacts_of_email'", 'db_column': "u'email_address_id'", 'to': u"orm['sugarmodels.EmailAddress']"}),
            'email_contacts_id': ('django_uuid.fields.UUIDField', [], {'max_length': '36', 'primary_key': 'True', 'db_column': "u'id'"}),
            'primary_address': ('django.db.models.fields.IntegerField', [], {'default': '1', 'null': 'True', 'blank': 'True'}),
            'reply_to_address': ('django.db.models.fields.IntegerField', [], {'default': '0', 'null': 'True', 'blank': 'True'})
        },
        u'sugarmodels.sugaruser': {
            'Meta': {'object_name': 'SugarUser', 'db_table': "u'users'", 'managed': 'False'},
            'address_city': ('django.db.models.fields.CharField', [], {'max_length': '100L', 'blank': 'True'}),
            'address_country': ('django.db.models.fields.CharField', [], {'max_length': '100L', 'blank': 'True'}),
            'address_postalcode': ('django.db.models.fields.CharField', [], {'max_length': '20L', 'blank': 'True'}),
            'address_state': ('django.db.models.fields.CharField', [], {'max_length': '100L', 'blank': 'True'}),
            'address_street': ('django.db.models.fields.CharField', [], {'max_length': '150L', 'blank': 'True'}),
            'authenticate_id': ('django.db.models.fields.CharField', [], {'max_length': '100L', 'blank': 'True'}),
            'created_by': ('django.db.models.fields.CharField', [], {'max_length': '36L', 'blank': 'True'}),
            'date_entered': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'date_modified': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'deleted': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'department': ('django.db.models.fields.CharField', [], {'max_length': '50L', 'blank': 'True'}),
            'description': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'employee_status': ('django.db.models.fields.CharField', [], {'max_length': '100L', 'blank': 'True'}),
            'external_auth_only': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '30L', 'blank': 'True'}),
            'id': ('django_uuid.fields.UUIDField', [], {'max_length': '36', 'primary_key': 'True'}),
            'is_admin': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'is_group': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '30L', 'blank': 'True'}),
            'messenger_id': ('django.db.models.fields.CharField', [], {'max_length': '100L', 'blank': 'True'}),
            'messenger_type': ('django.db.models.fields.CharField', [], {'max_length': '100L', 'blank': 'True'}),
            'modified_user_id': ('django.db.models.fields.CharField', [], {'max_length': '36L', 'blank': 'True'}),
            'phone_fax': ('django.db.models.fields.CharField', [], {'max_length': '50L', 'blank': 'True'}),
            'phone_home': ('django.db.models.fields.CharField', [], {'max_length': '50L', 'blank': 'True'}),
            'phone_mobile': ('django.db.models.fields.CharField', [], {'max_length': '50L', 'blank': 'True'}),
            'phone_other': ('django.db.models.fields.CharField', [], {'max_length': '50L', 'blank': 'True'}),
            'phone_work': ('django.db.models.fields.CharField', [], {'max_length': '50L', 'blank': 'True'}),
            'portal_only': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'pwd_last_changed': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            'receive_notifications': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'reports_to_id': ('django.db.models.fields.CharField', [], {'max_length': '36L', 'blank': 'True'}),
            'show_on_employees': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'status': ('django.db.models.fields.CharField', [], {'max_length': '100L', 'blank': 'True'}),
            'sugar_login': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'system_generated_password': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '50L', 'blank': 'True'}),
            'user_hash': ('django.db.models.fields.CharField', [], {'max_length': '255L', 'blank': 'True'}),
            'user_name': ('django.db.models.fields.CharField', [], {'max_length': '60L', 'blank': 'True'})
        }
    }

    complete_apps = ['sugarlink']