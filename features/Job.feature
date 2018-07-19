Feature: Apply for Job
 In order to search for suitable job opportunity,
 As a applicant
 Become a premium subscriber or 
 Use free trial

  Scenario: Home Page
     Given Become a premium member or direct apply 
      When I fetch home page
      Then Create your profile else apply directly


  Scenario: Free trial
     Given Provide your details 
      When Submit your resume along with contact details
      Then Applied successfully


  Scenario: Premium Users
	 Given First time user create an account or existing user can login
	  When Applicant will access the account
      Then Contact directly to the Hr and Track the application status


  Scenario Outline: Dashboard Functionality
   Given Consider a user "<username>"
    When User perform actions 
    Then The user "<username>" has "<user_type>" account

  Examples:
  | username | user_type |
  | Admin   | Premium  |
  | John    | Free   |




