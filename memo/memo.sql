SQLite format 3   @     <                                                               < .O}�  "�                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    ��tablemoviemovieCREATE TABLE movie (
	movie_id INTEGER NOT NULL, 
	user_id INTEGER NOT NULL, 
	rating FLOAT NOT NULL, 
	description VARCHAR(240) NOT NULL, 
	time_added DATETIME NOT NULL, 
	genre VARCHAR(50) NOT NULL, 
	title VARCHAR(100) NOT NULL, 
	PRIMARY KEY (movie_id)
)�*�7tableuseruserCREATE TABLE user (
	id INTEGER NOT NULL, 
	username VARCHAR(30) NOT NULL, 
	password VARCHAR(60) NOT NULL, 
	PRIMARY KEY (id), 
	UNIQUE (username)
)'; indexsqlite_autoindex_user_1user          : ��:                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          p �Yleilapbkdf2:sha256:260000$uHpsUVDVBLGtJiui$c2a93fa9f0ebed3c1cf6f12ed6f69db2ebc86cf9cd5fb9577525e0a92e334dfbp �Ytest3pbkdf2:sha256:260000$v6xBOIjJWKOc0ray$52e350e27ac6af30b36a6cdad998bcc4447acaa0e297df6ae9fc21efc5db0997o �Ytestpbkdf2:sha256:260000$VTd2JMbcnWDhN3uP$13235f47c81d445722be5b3bb7f607bbc296934c5ffbe48858f1d0c82c83561eo �Yhadipbkdf2:sha256:260000$MbH12i8pUWfe00ok$2759182b6ecaf6dbf7207d85b3f82ab69a549eab3e9ba0bcb64477bdb7d4da4f
   � ����                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           	leila	test3test	hadi� ] ]]'�                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               Y	?A)@      harry potter 2 movie desc2021-08-28 18:27:32.434734A   Z9A/@      test 3 movie diff desc2021-08-28 19:11:42.737869Horrortest 3 movie diff   P/A%   U?A!@      talking about Alzheimer  2021-08-28b 	WA3Pre Production Test Movie Description2021-08-29 11:53:19.189364FictionPre Production test   ?	A@      test desc2021-08-28 18:45:15.909248Actiontest