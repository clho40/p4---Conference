#!/usr/bin/env python

"""
main.py -- Udacity conference server-side Python App Engine
    HTTP controller handlers for memcache & task queue access

$Id$

created by wesc on 2014 may 24

"""

__author__ = 'wesc+api@google.com (Wesley Chun)'

import webapp2
from google.appengine.api import app_identity
from google.appengine.api import mail
from google.appengine.api import memcache
from conference import ConferenceApi
from models import Session

class SetAnnouncementHandler(webapp2.RequestHandler):
    def get(self):
        """Set Announcement in Memcache."""
        ConferenceApi._cacheAnnouncement()
        self.response.set_status(204)


class SendConfirmationEmailHandler(webapp2.RequestHandler):
    def post(self):
        """Send email confirming Conference creation."""
        mail.send_mail(
            'noreply@%s.appspotmail.com' % (
                app_identity.get_application_id()),     # from
            self.request.get('email'),                  # to
            'You created a new Conference!',            # subj
            'Hi, you have created a following '         # body
            'conference:\r\n\r\n%s' % self.request.get(
                'conferenceInfo')
        )

# - - - Task 3 - Add a Task - - - - - - - - - - - - - - - - - - - -     
class setFeaturedSpeaker(webapp2.RequestHandler):
    def post(self):
        """Set Featured Speaker in Memcache."""
        conference_key = self.request.get('conference_key')
        speaker_id = self.request.get('speaker_id')
        session_name = self.request.get('session_name')
        q = Session.query(Session.websafeConferenceKey == conference_key, Session.speaker == speaker_id)
        sessions = q.fetch()
        #if there is more than one record means the speaker is 
        #conducting more than one session in the conference.
        if sessions and q.count() > 1:
            featured_speaker = 'SPEAKER:%s , SESSION:%s ' %(speaker_id,session_name)
            memcache.set('FEATURED_SPEAKER',featured_speaker)   
        
app = webapp2.WSGIApplication([
    ('/crons/set_announcement', SetAnnouncementHandler),
    ('/tasks/send_confirmation_email', SendConfirmationEmailHandler),
    ('/tasks/set_featured_speaker', setFeaturedSpeaker),
], debug=True)
