# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Deleting field 'MapCelestialStatistic.luminousity'
        db.delete_column('eve_db_mapcelestialstatistic', 'luminousity')

        # Adding field 'MapCelestialStatistic.luminosity'
        db.add_column('eve_db_mapcelestialstatistic', 'luminosity', self.gf('django.db.models.fields.FloatField')(null=True, blank=True), keep_default=False)


    def backwards(self, orm):
        
        # Adding field 'MapCelestialStatistic.luminousity'
        db.add_column('eve_db_mapcelestialstatistic', 'luminousity', self.gf('django.db.models.fields.FloatField')(null=True, blank=True), keep_default=False)

        # Deleting field 'MapCelestialStatistic.luminosity'
        db.delete_column('eve_db_mapcelestialstatistic', 'luminosity')


    models = {
        'eve_api.apiplayeralliance': {
            'Meta': {'ordering': "['date_founded']", 'object_name': 'ApiPlayerAlliance'},
            'api_last_updated': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            'date_founded': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'member_count': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'ticker': ('django.db.models.fields.CharField', [], {'max_length': '15', 'blank': 'True'})
        },
        'eve_db.agtagent': {
            'Meta': {'ordering': "['id']", 'object_name': 'AgtAgent'},
            'corporation': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['eve_db.CrpNPCCorporation']", 'null': 'True', 'blank': 'True'}),
            'division': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['eve_db.CrpNPCDivision']", 'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.IntegerField', [], {'unique': 'True', 'primary_key': 'True'}),
            'level': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'location': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['eve_db.MapDenormalize']", 'null': 'True', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'quality': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'type': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['eve_db.AgtAgentType']", 'null': 'True', 'blank': 'True'})
        },
        'eve_db.agtagenttype': {
            'Meta': {'ordering': "['id']", 'object_name': 'AgtAgentType'},
            'id': ('django.db.models.fields.IntegerField', [], {'unique': 'True', 'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        },
        'eve_db.agtconfig': {
            'Meta': {'ordering': "['id']", 'unique_together': "(('agent', 'key'),)", 'object_name': 'AgtConfig'},
            'agent': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['eve_db.AgtAgent']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'key': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'value': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'})
        },
        'eve_db.chrancestry': {
            'Meta': {'ordering': "['id']", 'object_name': 'ChrAncestry'},
            'bloodline': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['eve_db.ChrBloodline']", 'null': 'True', 'blank': 'True'}),
            'charisma_bonus': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'description': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'icon': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['eve_db.EveIcon']", 'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.IntegerField', [], {'unique': 'True', 'primary_key': 'True'}),
            'intelligence_bonus': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'memory_bonus': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'perception_bonus': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'short_description': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'willpower_bonus': ('django.db.models.fields.IntegerField', [], {'default': '0'})
        },
        'eve_db.chrattribute': {
            'Meta': {'ordering': "['id']", 'object_name': 'ChrAttribute'},
            'description': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'icon': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['eve_db.EveIcon']", 'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.IntegerField', [], {'unique': 'True', 'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'notes': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'short_description': ('django.db.models.fields.TextField', [], {'blank': 'True'})
        },
        'eve_db.chrbloodline': {
            'Meta': {'ordering': "['id']", 'object_name': 'ChrBloodline'},
            'corporation': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['eve_db.CrpNPCCorporation']", 'null': 'True', 'blank': 'True'}),
            'description': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'female_description': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'icon': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['eve_db.EveIcon']", 'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.IntegerField', [], {'unique': 'True', 'primary_key': 'True'}),
            'male_description': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'race': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'bloodline_set'", 'null': 'True', 'to': "orm['eve_db.ChrRace']"}),
            'short_description': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'short_female_description': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'short_male_description': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'starter_ship_type': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'bloodline_starter_ship_set'", 'null': 'True', 'to': "orm['eve_db.InvType']"}),
            'starting_charisma': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'starting_intelligence': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'starting_memory': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'starting_perception': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'starting_willpower': ('django.db.models.fields.IntegerField', [], {'default': '0'})
        },
        'eve_db.chrfaction': {
            'Meta': {'ordering': "['id']", 'object_name': 'ChrFaction'},
            'corporation': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'faction_set'", 'null': 'True', 'to': "orm['eve_db.CrpNPCCorporation']"}),
            'description': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'icon': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['eve_db.EveIcon']", 'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.IntegerField', [], {'unique': 'True', 'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'size_factor': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'solar_system': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'faction_set'", 'null': 'True', 'to': "orm['eve_db.MapSolarSystem']"}),
            'station_count': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'station_system_count': ('django.db.models.fields.IntegerField', [], {'default': '0'})
        },
        'eve_db.chrrace': {
            'Meta': {'ordering': "['id']", 'object_name': 'ChrRace'},
            'description': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'icon': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['eve_db.EveIcon']", 'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.IntegerField', [], {'unique': 'True', 'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            'short_description': ('django.db.models.fields.TextField', [], {'blank': 'True'})
        },
        'eve_db.crpactivity': {
            'Meta': {'ordering': "['id']", 'object_name': 'CrpActivity'},
            'description': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'id': ('django.db.models.fields.IntegerField', [], {'unique': 'True', 'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        'eve_db.crpnpccorporation': {
            'Meta': {'ordering': "['id']", 'object_name': 'CrpNPCCorporation'},
            'border_systems': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'corridor_systems': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'description': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'enemy_corp': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'enemy_of_set'", 'null': 'True', 'to': "orm['eve_db.CrpNPCCorporation']"}),
            'extent': ('django.db.models.fields.CharField', [], {'max_length': '1', 'blank': 'True'}),
            'faction': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['eve_db.ChrFaction']", 'null': 'True', 'blank': 'True'}),
            'friendly_corp': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'friendly_with_set'", 'null': 'True', 'to': "orm['eve_db.CrpNPCCorporation']"}),
            'fringe_systems': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'hub_systems': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'icon': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['eve_db.EveIcon']", 'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.IntegerField', [], {'unique': 'True', 'primary_key': 'True'}),
            'initial_share_price': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'investor1': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'invested1_set'", 'null': 'True', 'to': "orm['eve_db.CrpNPCCorporation']"}),
            'investor1_shares': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'investor2': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'invested2_set'", 'null': 'True', 'to': "orm['eve_db.CrpNPCCorporation']"}),
            'investor2_shares': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'investor3': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'invested3_set'", 'null': 'True', 'to': "orm['eve_db.CrpNPCCorporation']"}),
            'investor3_shares': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'investor4': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'invested4_set'", 'null': 'True', 'to': "orm['eve_db.CrpNPCCorporation']"}),
            'investor4_shares': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'min_security': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'public_share_percent': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'size': ('django.db.models.fields.CharField', [], {'max_length': '1', 'blank': 'True'}),
            'size_factor': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'solar_system': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['eve_db.MapSolarSystem']", 'null': 'True', 'blank': 'True'}),
            'station_count': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'station_system_count': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'stations_are_scattered': ('django.db.models.fields.BooleanField', [], {'default': 'False'})
        },
        'eve_db.crpnpccorporationdivision': {
            'Meta': {'ordering': "['id']", 'unique_together': "(('corporation', 'division'),)", 'object_name': 'CrpNPCCorporationDivision'},
            'corporation': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['eve_db.CrpNPCCorporation']"}),
            'division': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['eve_db.CrpNPCDivision']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'size': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'})
        },
        'eve_db.crpnpccorporationresearchfield': {
            'Meta': {'ordering': "['id']", 'unique_together': "(('skill', 'corporation'),)", 'object_name': 'CrpNPCCorporationResearchField'},
            'corporation': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['eve_db.CrpNPCCorporation']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'skill': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['eve_db.InvType']", 'null': 'True', 'blank': 'True'})
        },
        'eve_db.crpnpccorporationtrade': {
            'Meta': {'ordering': "['id']", 'unique_together': "(('corporation', 'type'),)", 'object_name': 'CrpNPCCorporationTrade'},
            'corporation': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['eve_db.CrpNPCCorporation']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'type': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['eve_db.InvType']", 'null': 'True', 'blank': 'True'})
        },
        'eve_db.crpnpcdivision': {
            'Meta': {'ordering': "['id']", 'object_name': 'CrpNPCDivision'},
            'description': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'id': ('django.db.models.fields.IntegerField', [], {'unique': 'True', 'primary_key': 'True'}),
            'leader_type': ('django.db.models.fields.CharField', [], {'max_length': '100', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100', 'blank': 'True'})
        },
        'eve_db.crtcategory': {
            'Meta': {'ordering': "['id']", 'object_name': 'CrtCategory'},
            'description': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'id': ('django.db.models.fields.IntegerField', [], {'unique': 'True', 'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'})
        },
        'eve_db.crtcertificate': {
            'Meta': {'ordering': "['id']", 'object_name': 'CrtCertificate'},
            'category': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['eve_db.CrtCategory']", 'null': 'True', 'blank': 'True'}),
            'cert_class': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['eve_db.CrtClass']", 'null': 'True', 'blank': 'True'}),
            'corporation': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['eve_db.CrpNPCCorporation']", 'null': 'True', 'blank': 'True'}),
            'description': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'grade': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'icon_num': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.IntegerField', [], {'unique': 'True', 'primary_key': 'True'})
        },
        'eve_db.crtclass': {
            'Meta': {'ordering': "['id']", 'object_name': 'CrtClass'},
            'description': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'id': ('django.db.models.fields.IntegerField', [], {'unique': 'True', 'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'})
        },
        'eve_db.crtrecommendation': {
            'Meta': {'ordering': "['id']", 'object_name': 'CrtRecommendation'},
            'certificate': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['eve_db.CrtCertificate']", 'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.IntegerField', [], {'unique': 'True', 'primary_key': 'True'}),
            'recommendation_level': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'ship_type': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['eve_db.InvType']", 'null': 'True', 'blank': 'True'})
        },
        'eve_db.crtrelationship': {
            'Meta': {'ordering': "['id']", 'object_name': 'CrtRelationship'},
            'child': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'child_crtrelationship_set'", 'null': 'True', 'to': "orm['eve_db.CrtCertificate']"}),
            'id': ('django.db.models.fields.IntegerField', [], {'unique': 'True', 'primary_key': 'True'}),
            'parent': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'parent_crtrelationship_set'", 'null': 'True', 'to': "orm['eve_db.CrtCertificate']"}),
            'parent_level': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'parent_type': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['eve_db.InvType']", 'null': 'True', 'blank': 'True'})
        },
        'eve_db.dgmattributecategory': {
            'Meta': {'ordering': "['id']", 'object_name': 'DgmAttributeCategory'},
            'description': ('django.db.models.fields.CharField', [], {'max_length': '100', 'blank': 'True'}),
            'id': ('django.db.models.fields.IntegerField', [], {'unique': 'True', 'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '30'})
        },
        'eve_db.dgmattributetype': {
            'Meta': {'ordering': "['id']", 'object_name': 'DgmAttributeType'},
            'category': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['eve_db.DgmAttributeCategory']", 'null': 'True', 'blank': 'True'}),
            'defaultvalue': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'description': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'display_name': ('django.db.models.fields.CharField', [], {'max_length': '100', 'blank': 'True'}),
            'high_is_good': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'icon': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['eve_db.EveIcon']", 'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.IntegerField', [], {'unique': 'True', 'primary_key': 'True'}),
            'is_published': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_stackable': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '75'}),
            'unit': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['eve_db.EveUnit']", 'null': 'True', 'blank': 'True'})
        },
        'eve_db.dgmeffect': {
            'Meta': {'ordering': "['id']", 'object_name': 'DgmEffect'},
            'category': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'description': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'disallow_auto_repeat': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'discharge_attribute': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'inventoryeffectdischargeattribute'", 'null': 'True', 'to': "orm['eve_db.DgmAttributeType']"}),
            'display_name': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'distribution': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'duration_attribute': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'inventoryeffectdurationeattribute'", 'null': 'True', 'to': "orm['eve_db.DgmAttributeType']"}),
            'falloff_attribute': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'inventoryeffectfalloffattribute'", 'null': 'True', 'to': "orm['eve_db.DgmAttributeType']"}),
            'fitting_usage_chance_attribute': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'inventoryeffectfittingusagechanceattribute'", 'null': 'True', 'to': "orm['eve_db.DgmAttributeType']"}),
            'guid': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'has_electronic_chance': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'has_propulsion_chance': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'has_range_chance': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'icon': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['eve_db.EveIcon']", 'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.IntegerField', [], {'unique': 'True', 'primary_key': 'True'}),
            'is_assistance': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_offensive': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_published': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_warp_safe': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '150'}),
            'npc_activation_chance_attribute': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'inventoryeffectnpcactivationchanceattribute'", 'null': 'True', 'to': "orm['eve_db.DgmAttributeType']"}),
            'npc_usage_chance_attribute': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'inventoryeffectnpcusagechanceattribute'", 'null': 'True', 'to': "orm['eve_db.DgmAttributeType']"}),
            'post_expression': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'pre_expression': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'range_attribute': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'inventoryeffectrangeattribute'", 'null': 'True', 'to': "orm['eve_db.DgmAttributeType']"}),
            'sfx_name': ('django.db.models.fields.CharField', [], {'max_length': '100', 'blank': 'True'}),
            'tracking_speed_attribute': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'inventoryeffecttrackingspeedattribute'", 'null': 'True', 'to': "orm['eve_db.DgmAttributeType']"})
        },
        'eve_db.dgmtypeattribute': {
            'Meta': {'ordering': "['id']", 'unique_together': "(('inventory_type', 'attribute'),)", 'object_name': 'DgmTypeAttribute'},
            'attribute': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['eve_db.DgmAttributeType']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'inventory_type': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['eve_db.InvType']"}),
            'value_float': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'value_int': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'})
        },
        'eve_db.dgmtypeeffect': {
            'Meta': {'ordering': "['id']", 'unique_together': "(('type', 'effect'),)", 'object_name': 'DgmTypeEffect'},
            'effect': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['eve_db.DgmEffect']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_default': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'type': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['eve_db.InvType']"})
        },
        'eve_db.evegraphic': {
            'Meta': {'ordering': "['id']", 'object_name': 'EveGraphic'},
            'description': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'file': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'id': ('django.db.models.fields.IntegerField', [], {'unique': 'True', 'primary_key': 'True'}),
            'is_obsolete': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        'eve_db.eveicon': {
            'Meta': {'ordering': "['id']", 'object_name': 'EveIcon'},
            'description': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'file': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'id': ('django.db.models.fields.IntegerField', [], {'unique': 'True', 'primary_key': 'True'})
        },
        'eve_db.evename': {
            'Meta': {'ordering': "['id']", 'object_name': 'EveName'},
            'category': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['eve_db.InvCategory']", 'null': 'True', 'blank': 'True'}),
            'group': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['eve_db.InvGroup']", 'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.IntegerField', [], {'unique': 'True', 'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'type': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['eve_db.InvType']", 'null': 'True', 'blank': 'True'})
        },
        'eve_db.eveunit': {
            'Meta': {'ordering': "['id']", 'object_name': 'EveUnit'},
            'description': ('django.db.models.fields.CharField', [], {'max_length': '100', 'blank': 'True'}),
            'display_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'id': ('django.db.models.fields.IntegerField', [], {'unique': 'True', 'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '75'})
        },
        'eve_db.invblueprinttype': {
            'Meta': {'ordering': "['blueprint_type']", 'object_name': 'InvBlueprintType'},
            'blueprint_type': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'blueprint_type_set'", 'unique': 'True', 'primary_key': 'True', 'to': "orm['eve_db.InvType']"}),
            'material_modifier': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'max_production_limit': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'parent_blueprint_type': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'parent_blueprint_type_set'", 'null': 'True', 'to': "orm['eve_db.InvType']"}),
            'product_type': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'blueprint_product_type_set'", 'to': "orm['eve_db.InvType']"}),
            'productivity_modifier': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'research_copy_time': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'research_material_time': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'research_productivity_time': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'research_tech_time': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'tech_level': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'waste_factor': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'})
        },
        'eve_db.invcategory': {
            'Meta': {'ordering': "['id']", 'object_name': 'InvCategory'},
            'description': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'icon': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['eve_db.EveIcon']", 'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.IntegerField', [], {'unique': 'True', 'primary_key': 'True'}),
            'is_published': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        'eve_db.invcontrabandtype': {
            'Meta': {'ordering': "['id']", 'unique_together': "(('faction', 'type'),)", 'object_name': 'InvContrabandType'},
            'attack_min_sec': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'confiscate_min_sec': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'faction': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['eve_db.ChrFaction']"}),
            'fine_by_value': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'standing_loss': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'type': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['eve_db.InvType']"})
        },
        'eve_db.invflag': {
            'Meta': {'ordering': "['id']", 'object_name': 'InvFlag'},
            'id': ('django.db.models.fields.IntegerField', [], {'unique': 'True', 'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'order': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'text': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'type_text': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'})
        },
        'eve_db.invgroup': {
            'Meta': {'ordering': "['id']", 'object_name': 'InvGroup'},
            'allow_anchoring': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'allow_manufacture': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'allow_recycle': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'category': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['eve_db.InvCategory']", 'null': 'True', 'blank': 'True'}),
            'description': ('django.db.models.fields.TextField', [], {}),
            'icon': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['eve_db.EveIcon']", 'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.IntegerField', [], {'unique': 'True', 'primary_key': 'True'}),
            'is_anchored': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_fittable_non_singleton': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_published': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '150'}),
            'use_base_price': ('django.db.models.fields.BooleanField', [], {'default': 'False'})
        },
        'eve_db.invmarketgroup': {
            'Meta': {'ordering': "['id']", 'object_name': 'InvMarketGroup'},
            'description': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'has_items': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'icon': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['eve_db.EveIcon']", 'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.IntegerField', [], {'unique': 'True', 'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'parent': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['eve_db.InvMarketGroup']", 'null': 'True', 'blank': 'True'})
        },
        'eve_db.invmetagroup': {
            'Meta': {'ordering': "['id']", 'object_name': 'InvMetaGroup'},
            'description': ('django.db.models.fields.TextField', [], {}),
            'icon': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['eve_db.EveIcon']", 'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.IntegerField', [], {'unique': 'True', 'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        },
        'eve_db.invmetatype': {
            'Meta': {'ordering': "['type']", 'object_name': 'InvMetaType'},
            'meta_group': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['eve_db.InvMetaGroup']"}),
            'parent_type': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'inventorymetatype_parent_type_set'", 'to': "orm['eve_db.InvType']"}),
            'type': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'inventorymetatype_type_set'", 'unique': 'True', 'primary_key': 'True', 'to': "orm['eve_db.InvType']"})
        },
        'eve_db.invposresource': {
            'Meta': {'ordering': "['id']", 'unique_together': "(('control_tower_type', 'resource_type'),)", 'object_name': 'InvPOSResource'},
            'control_tower_type': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'tower_resource_set'", 'to': "orm['eve_db.InvType']"}),
            'faction': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['eve_db.ChrFaction']", 'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'min_security_level': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'purpose': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['eve_db.InvPOSResourcePurpose']", 'null': 'True', 'blank': 'True'}),
            'quantity': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'resource_type': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'pos_resource_set'", 'to': "orm['eve_db.InvType']"})
        },
        'eve_db.invposresourcepurpose': {
            'Meta': {'ordering': "['id']", 'object_name': 'InvPOSResourcePurpose'},
            'id': ('django.db.models.fields.IntegerField', [], {'unique': 'True', 'primary_key': 'True'}),
            'purpose': ('django.db.models.fields.CharField', [], {'max_length': '75', 'blank': 'True'})
        },
        'eve_db.invtype': {
            'Meta': {'ordering': "['id']", 'object_name': 'InvType'},
            'base_price': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'capacity': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'chance_of_duplicating': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'description': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'graphic': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['eve_db.EveGraphic']", 'null': 'True', 'blank': 'True'}),
            'group': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['eve_db.InvGroup']", 'null': 'True', 'blank': 'True'}),
            'icon': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['eve_db.EveIcon']", 'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.IntegerField', [], {'unique': 'True', 'primary_key': 'True'}),
            'is_published': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'market_group': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['eve_db.InvMarketGroup']", 'null': 'True', 'blank': 'True'}),
            'mass': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100', 'blank': 'True'}),
            'portion_size': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'race': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['eve_db.ChrRace']", 'null': 'True', 'blank': 'True'}),
            'radius': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'volume': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'})
        },
        'eve_db.invtypematerial': {
            'Meta': {'ordering': "['id']", 'unique_together': "(('type', 'material_type'),)", 'object_name': 'InvTypeMaterial'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'material_type': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'itemtype_set'", 'to': "orm['eve_db.InvType']"}),
            'quantity': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'type': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'material_set'", 'to': "orm['eve_db.InvType']"})
        },
        'eve_db.invtypereaction': {
            'Meta': {'ordering': "['id']", 'unique_together': "(('reaction_type', 'input', 'type'),)", 'object_name': 'InvTypeReaction'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'input': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'quantity': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'reaction_type': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'inventorytypereactions_reaction_type_set'", 'to': "orm['eve_db.InvType']"}),
            'type': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'inventorytypereactions_type_set'", 'to': "orm['eve_db.InvType']"})
        },
        'eve_db.mapcelestialstatistic': {
            'Meta': {'ordering': "['celestial']", 'object_name': 'MapCelestialStatistic'},
            'age': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'celestial': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['eve_db.MapDenormalize']", 'unique': 'True', 'primary_key': 'True'}),
            'density': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'eccentricity': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'escape_velocity': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'is_fragmented': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_locked': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'life': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'luminosity': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'mass': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'mass_dust': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'mass_gas': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'orbit_period': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'orbit_radius': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'pressure': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'radius': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'rotation_rate': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'spectral_class': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'surface_gravity': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'temperature': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'})
        },
        'eve_db.mapconstellation': {
            'Meta': {'ordering': "['id']", 'object_name': 'MapConstellation'},
            'alliance': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['eve_api.ApiPlayerAlliance']", 'null': 'True', 'blank': 'True'}),
            'faction': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['eve_db.ChrFaction']", 'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.IntegerField', [], {'unique': 'True', 'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'radius': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'region': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['eve_db.MapRegion']", 'null': 'True', 'blank': 'True'}),
            'sovereignty_grace_start_time': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            'sovereignty_start_time': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            'x': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'x_max': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'x_min': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'y': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'y_max': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'y_min': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'z': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'z_max': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'z_min': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'})
        },
        'eve_db.mapconstellationjump': {
            'Meta': {'ordering': "['id']", 'unique_together': "(('from_constellation', 'to_constellation'),)", 'object_name': 'MapConstellationJump'},
            'from_constellation': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'constellation_jumps_from_constellation_set'", 'to': "orm['eve_db.MapConstellation']"}),
            'from_region': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'constellation_jumps_from_region_set'", 'to': "orm['eve_db.MapRegion']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'to_constellation': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'constellation_jumps_to_constellation_set'", 'to': "orm['eve_db.MapConstellation']"}),
            'to_region': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'constellation_jumps_to_region_set'", 'to': "orm['eve_db.MapRegion']"})
        },
        'eve_db.mapdenormalize': {
            'Meta': {'ordering': "['id']", 'object_name': 'MapDenormalize'},
            'celestial_index': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'constellation': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['eve_db.MapConstellation']", 'null': 'True', 'blank': 'True'}),
            'group': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['eve_db.InvGroup']", 'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.IntegerField', [], {'unique': 'True', 'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'orbit_id': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'orbit_index': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'radius': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'region': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['eve_db.MapRegion']", 'null': 'True', 'blank': 'True'}),
            'security': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'solar_system': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['eve_db.MapSolarSystem']", 'null': 'True', 'blank': 'True'}),
            'type': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['eve_db.InvType']", 'null': 'True', 'blank': 'True'}),
            'x': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'y': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'z': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'})
        },
        'eve_db.mapjump': {
            'Meta': {'ordering': "['origin_gate']", 'object_name': 'MapJump'},
            'destination_gate': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'stargate_jump_destination_set'", 'to': "orm['eve_db.MapDenormalize']"}),
            'origin_gate': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'stargate_jump_origin_set'", 'unique': 'True', 'primary_key': 'True', 'to': "orm['eve_db.MapDenormalize']"})
        },
        'eve_db.maplandmark': {
            'Meta': {'ordering': "['id']", 'object_name': 'MapLandmark'},
            'description': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'icon': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['eve_db.EveIcon']", 'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.IntegerField', [], {'unique': 'True', 'primary_key': 'True'}),
            'importance': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'radius': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'solar_system': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['eve_db.MapSolarSystem']", 'null': 'True', 'blank': 'True'}),
            'x': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'y': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'z': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'})
        },
        'eve_db.mapregion': {
            'Meta': {'ordering': "['id']", 'object_name': 'MapRegion'},
            'faction': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['eve_db.ChrFaction']", 'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.IntegerField', [], {'unique': 'True', 'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'radius': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'x': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'x_max': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'x_min': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'y': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'y_max': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'y_min': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'z': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'z_max': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'z_min': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'})
        },
        'eve_db.mapregionjump': {
            'Meta': {'ordering': "['id']", 'unique_together': "(('from_region', 'to_region'),)", 'object_name': 'MapRegionJump'},
            'from_region': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'region_jumps_from_region_set'", 'to': "orm['eve_db.MapRegion']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'to_region': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'region_jumps_to_region_set'", 'to': "orm['eve_db.MapRegion']"})
        },
        'eve_db.mapsolarsystem': {
            'Meta': {'ordering': "['id']", 'object_name': 'MapSolarSystem'},
            'alliance': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['eve_api.ApiPlayerAlliance']", 'null': 'True', 'blank': 'True'}),
            'constellation': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['eve_db.MapConstellation']", 'null': 'True', 'blank': 'True'}),
            'faction': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'solarsystem_set'", 'null': 'True', 'to': "orm['eve_db.ChrFaction']"}),
            'has_interconstellational_link': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'has_interregional_link': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'id': ('django.db.models.fields.IntegerField', [], {'unique': 'True', 'primary_key': 'True'}),
            'is_border_system': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_corridor_system': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_fringe_system': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_hub_system': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_international': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'luminosity': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'radius': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'region': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['eve_db.MapRegion']", 'null': 'True', 'blank': 'True'}),
            'security_class': ('django.db.models.fields.CharField', [], {'max_length': '5', 'blank': 'True'}),
            'security_level': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'sovereignty_level': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'sovereignty_start_time': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            'sun_type': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['eve_db.InvType']", 'null': 'True', 'blank': 'True'}),
            'x': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'x_max': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'x_min': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'y': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'y_max': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'y_min': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'z': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'z_max': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'z_min': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'})
        },
        'eve_db.mapsolarsystemjump': {
            'Meta': {'ordering': "['id']", 'unique_together': "(('from_solar_system', 'to_solar_system'),)", 'object_name': 'MapSolarSystemJump'},
            'from_constellation': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'solar_system_jumps_from_constellation_set'", 'null': 'True', 'to': "orm['eve_db.MapConstellation']"}),
            'from_region': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'solar_system_jumps_from_region_set'", 'null': 'True', 'to': "orm['eve_db.MapRegion']"}),
            'from_solar_system': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'solar_system_jumps_from_solar_system_set'", 'to': "orm['eve_db.MapSolarSystem']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'to_constellation': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'solar_system_jumps_to_constellation_set'", 'null': 'True', 'to': "orm['eve_db.MapConstellation']"}),
            'to_region': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'solar_system_jumps_to_region_set'", 'null': 'True', 'to': "orm['eve_db.MapRegion']"}),
            'to_solar_system': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'solar_system_jumps_to_solar_system_set'", 'to': "orm['eve_db.MapSolarSystem']"})
        },
        'eve_db.mapuniverse': {
            'Meta': {'ordering': "['id']", 'object_name': 'MapUniverse'},
            'id': ('django.db.models.fields.IntegerField', [], {'unique': 'True', 'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'radius': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'x': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'x_max': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'x_min': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'y': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'y_max': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'y_min': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'z': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'z_max': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'z_min': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'})
        },
        'eve_db.planetschematic': {
            'Meta': {'ordering': "['id']", 'object_name': 'PlanetSchematic'},
            'cycle_time': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.IntegerField', [], {'unique': 'True', 'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'pin_map': ('django.db.models.fields.related.ManyToManyField', [], {'related_name': "'usable_schematics'", 'symmetrical': 'False', 'through': "orm['eve_db.PlanetSchematicsPinMap']", 'to': "orm['eve_db.InvType']"}),
            'type_map': ('django.db.models.fields.related.ManyToManyField', [], {'related_name': "'used_with_schematic'", 'symmetrical': 'False', 'through': "orm['eve_db.PlanetSchematicsTypeMap']", 'to': "orm['eve_db.InvType']"})
        },
        'eve_db.planetschematicspinmap': {
            'Meta': {'ordering': "['schematic', 'type']", 'unique_together': "(('schematic', 'type'),)", 'object_name': 'PlanetSchematicsPinMap'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'schematic': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['eve_db.PlanetSchematic']"}),
            'type': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['eve_db.InvType']"})
        },
        'eve_db.planetschematicstypemap': {
            'Meta': {'ordering': "['schematic', 'is_input', 'type']", 'unique_together': "(('schematic', 'type'),)", 'object_name': 'PlanetSchematicsTypeMap'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_input': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'quantity': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'schematic': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['eve_db.PlanetSchematic']"}),
            'type': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['eve_db.InvType']"})
        },
        'eve_db.ramactivity': {
            'Meta': {'ordering': "['id']", 'object_name': 'RamActivity'},
            'description': ('django.db.models.fields.CharField', [], {'max_length': '100', 'blank': 'True'}),
            'icon_filename': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.IntegerField', [], {'unique': 'True', 'primary_key': 'True'}),
            'is_published': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '75', 'blank': 'True'})
        },
        'eve_db.ramassemblyline': {
            'Meta': {'ordering': "['id']", 'object_name': 'RamAssemblyLine'},
            'activity': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['eve_db.RamActivity']", 'null': 'True', 'blank': 'True'}),
            'assembly_line_type': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['eve_db.RamAssemblyLineType']", 'null': 'True', 'blank': 'True'}),
            'cost_install': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'cost_per_hour': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'discount_per_good_standing_point': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.IntegerField', [], {'unique': 'True', 'primary_key': 'True'}),
            'maximum_char_security': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'maximum_corp_security': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'minimum_char_security': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'minimum_corp_security': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'minimum_standing': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'owner': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['eve_db.CrpNPCCorporation']", 'null': 'True', 'blank': 'True'}),
            'station': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['eve_db.StaStation']", 'null': 'True', 'blank': 'True'}),
            'surcharge_per_bad_standing_point': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'ui_grouping_id': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'})
        },
        'eve_db.ramassemblylinestations': {
            'Meta': {'ordering': "['id']", 'unique_together': "(('station', 'assembly_line_type'),)", 'object_name': 'RamAssemblyLineStations'},
            'assembly_line_type': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['eve_db.RamAssemblyLineType']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'owner': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['eve_db.CrpNPCCorporation']", 'null': 'True', 'blank': 'True'}),
            'quantity': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'region': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['eve_db.MapRegion']", 'null': 'True', 'blank': 'True'}),
            'solar_system': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['eve_db.MapSolarSystem']", 'null': 'True', 'blank': 'True'}),
            'station': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['eve_db.StaStation']"}),
            'station_type': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['eve_db.StaStationType']", 'null': 'True', 'blank': 'True'})
        },
        'eve_db.ramassemblylinetype': {
            'Meta': {'ordering': "['id']", 'object_name': 'RamAssemblyLineType'},
            'activity': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['eve_db.RamActivity']", 'null': 'True', 'blank': 'True'}),
            'base_material_multiplier': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'base_time_multiplier': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'description': ('django.db.models.fields.CharField', [], {'max_length': '100', 'blank': 'True'}),
            'id': ('django.db.models.fields.IntegerField', [], {'unique': 'True', 'primary_key': 'True'}),
            'min_cost_per_hour': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100', 'blank': 'True'}),
            'volume': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'})
        },
        'eve_db.ramassemblylinetypedetailpercategory': {
            'Meta': {'ordering': "['id']", 'unique_together': "(('assembly_line_type', 'category'),)", 'object_name': 'RamAssemblyLineTypeDetailPerCategory'},
            'assembly_line_type': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['eve_db.RamAssemblyLineType']"}),
            'category': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['eve_db.InvCategory']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'material_multiplier': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'time_multiplier': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'})
        },
        'eve_db.ramassemblylinetypedetailpergroup': {
            'Meta': {'ordering': "['id']", 'unique_together': "(('assembly_line_type', 'group'),)", 'object_name': 'RamAssemblyLineTypeDetailPerGroup'},
            'assembly_line_type': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['eve_db.RamAssemblyLineType']"}),
            'group': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['eve_db.InvGroup']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'material_multiplier': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'time_multiplier': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'})
        },
        'eve_db.ramtyperequirement': {
            'Meta': {'ordering': "['id']", 'unique_together': "(('type', 'activity_type', 'required_type'),)", 'object_name': 'RamTypeRequirement'},
            'activity_type': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['eve_db.RamActivity']"}),
            'damage_per_job': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'quantity': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'recycle': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'required_type': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'required_type'", 'to': "orm['eve_db.InvType']"}),
            'type': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'type_requirement'", 'to': "orm['eve_db.InvType']"})
        },
        'eve_db.staoperation': {
            'Meta': {'ordering': "['id']", 'object_name': 'StaOperation'},
            'activity_id': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'amarr_station_type': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'amarr_station_operation_set'", 'null': 'True', 'to': "orm['eve_db.StaStationType']"}),
            'border': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'caldari_station_type': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'caldari_station_operation_set'", 'null': 'True', 'to': "orm['eve_db.StaStationType']"}),
            'corridor': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'description': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'fringe': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'gallente_station_type': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'gallente_station_operation_set'", 'null': 'True', 'to': "orm['eve_db.StaStationType']"}),
            'hub': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.IntegerField', [], {'unique': 'True', 'primary_key': 'True'}),
            'jove_station_type': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'jove_station_operation_set'", 'null': 'True', 'to': "orm['eve_db.StaStationType']"}),
            'minmatar_station_type': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'minmatar_station_operation_set'", 'null': 'True', 'to': "orm['eve_db.StaStationType']"}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'ratio': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'})
        },
        'eve_db.staoperationservices': {
            'Meta': {'ordering': "['id']", 'unique_together': "(('operation', 'service'),)", 'object_name': 'StaOperationServices'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'operation': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['eve_db.StaOperation']"}),
            'service': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['eve_db.StaService']"})
        },
        'eve_db.staservice': {
            'Meta': {'ordering': "['id']", 'object_name': 'StaService'},
            'description': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'id': ('django.db.models.fields.IntegerField', [], {'unique': 'True', 'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        'eve_db.stastation': {
            'Meta': {'ordering': "['id']", 'object_name': 'StaStation'},
            'constellation': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['eve_db.MapConstellation']", 'null': 'True', 'blank': 'True'}),
            'corporation': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['eve_db.CrpNPCCorporation']", 'null': 'True', 'blank': 'True'}),
            'docking_cost_per_volume': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.IntegerField', [], {'unique': 'True', 'primary_key': 'True'}),
            'max_ship_volume_dockable': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100', 'blank': 'True'}),
            'office_rental_cost': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'operation': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['eve_db.StaOperation']", 'null': 'True', 'blank': 'True'}),
            'region': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['eve_db.MapRegion']", 'null': 'True', 'blank': 'True'}),
            'reprocessing_efficiency': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'reprocessing_hangar_flag': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'reprocessing_stations_take': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'security': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'solar_system': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['eve_db.MapSolarSystem']", 'null': 'True', 'blank': 'True'}),
            'type': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['eve_db.StaStationType']", 'null': 'True', 'blank': 'True'}),
            'x': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'y': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'z': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'})
        },
        'eve_db.stastationtype': {
            'Meta': {'ordering': "['id']", 'object_name': 'StaStationType'},
            'dock_entry_x': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'dock_entry_y': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'dock_entry_z': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'dock_orientation_x': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'dock_orientation_y': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'dock_orientation_z': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.IntegerField', [], {'unique': 'True', 'primary_key': 'True'}),
            'is_conquerable': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'office_slots': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'operation': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['eve_db.StaOperation']", 'null': 'True', 'blank': 'True'}),
            'reprocessing_efficiency': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'})
        }
    }

    complete_apps = ['eve_db']
