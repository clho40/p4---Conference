App Engine application for the Udacity training course.

## Products
- [App Engine][1]

## Language
- [Python][2]

## APIs
- [Google Cloud Endpoints][3]

## Setup Instructions
1. Update the value of `application` in `app.yaml` to the app ID you
   have registered in the App Engine admin console and would like to use to host
   your instance of this sample.
1. Update the values at the top of `settings.py` to
   reflect the respective client IDs you have registered in the
   [Developer Console][4].
1. Update the value of CLIENT_ID in `static/js/app.js` to the Web client ID
1. (Optional) Mark the configuration files as unchanged as follows:
   `$ git update-index --assume-unchanged app.yaml settings.py static/js/app.js`
1. Run the app with the devserver using `dev_appserver.py DIR`, and ensure it's running by visiting your local server's address (by default [localhost:8080][5].)
1. (Optional) Generate your client library(ies) with [the endpoints tool][6].
1. Deploy your application.

## Task 1 - Design Choices
1. Each Conference will contain multiple Sessions.
1. Each Sessions will be conducted by one Speaker.
1. Sessions organizer is expected to register the Speaker conducting the session, before the session is created.
1. Each Speakers will be assigned by an ID.
1. In sessions creation page, Speaker selection is expected to be handled in front-end (eg: a drop down list to select speaker by speaker's name)
1. The ID of selected Speaker will be saved into the Session entity.
1. The reason of registering a Speaker and having an entity of Speaker is to store the related information of the speaker (eg: qualification, organization, and etc) so that our application can make good use of these information to attract more people to take part in the conferences & sessions.

Datatype Choices
1. StringProperty - For fields that contains combination of alphanumeric and symbols
1. IntegerProperty - For fields that ONLY contains positive whole number
1. DateProperty - For fields that contains date information (eg: 1/12/2015)
1. TimeProperty - For fields that contains time information (eg: 19:00)

Properties in Speaker's Entity
1. name - String Field - A name consist a combination of alphabets and symbols (eg: Single quote - Conan O' Brian), therefore it is a string property.
1. email - String Field - An email consist of a combination of alphanumeric and symbols (eg: abc@def.com), therefore it is a string property.
1. qualification - Repeated String Field - A qualification consist of a combination of alphanumeric and symbols (eg: BEng in Electronic Engineering Year 2000) and a speaker can have multiple qualification, therefore it is a repeated string field.
1. working experience - Repeated String Field - Working Experience consist of a combination of alphanumeric and symbols (eg: Intel, 2000-Present) and a speaker can have multiple qualification, therefore it is a repeated string field.




## Task 2 - Additional Queries
1. getAllSpeakers - In order to bind all the speakers to a drop down list in front end page when creating session, it is necessary to retrieve all the speakers
1. getPotentialSessionAttendee - This query is to get the users that added the particular session into their wishlist, so that the organizer can contact them and get them to join the session!

## Task 3 - Query Problem
1. Datastore has limitation - Only one property type is allowed in inequality filter.
1. Therefore, in order to filter 2 inequalities: typeOfSession != "WORKSHOP" and startTime < 7pm, some workaround is needed!
1. Workaround - Filter each condition seperately, and get the intersection of both filtered query results (intersection of both query results gives the result of both condition satisfied)
              - This workout is already implemented in conference.py (refer to filterPlayground2 API endpoints)           



[1]: https://developers.google.com/appengine
[2]: http://python.org
[3]: https://developers.google.com/appengine/docs/python/endpoints/
[4]: https://console.developers.google.com/
[5]: https://localhost:8080/
[6]: https://developers.google.com/appengine/docs/python/endpoints/endpoints_tool
