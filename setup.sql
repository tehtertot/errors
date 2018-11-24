use dojo_errors;

ALTER TABLE `dojo_errors`.`languages` 
CHANGE COLUMN `created_at` `created_at` DATETIME NOT NULL DEFAULT now() ,
CHANGE COLUMN `updated_at` `updated_at` DATETIME NOT NULL DEFAULT now() on update now() ;
ALTER TABLE `dojo_errors`.`technologies` 
CHANGE COLUMN `created_at` `created_at` DATETIME NOT NULL DEFAULT now() ,
CHANGE COLUMN `updated_at` `updated_at` DATETIME NOT NULL DEFAULT now() on update now() ;
ALTER TABLE `dojo_errors`.`monthly_stacks` 
CHANGE COLUMN `created_at` `created_at` DATETIME NOT NULL DEFAULT now() ,
CHANGE COLUMN `updated_at` `updated_at` DATETIME NOT NULL DEFAULT now() on update now() ;
ALTER TABLE `dojo_errors`.`error_messages` 
CHANGE COLUMN `created_at` `created_at` DATETIME NOT NULL DEFAULT now() ,
CHANGE COLUMN `updated_at` `updated_at` DATETIME NOT NULL DEFAULT now() on update now() ;


-- ADDING LANGUAGES

INSERT INTO languages (name) VALUES ('Python'), ('C#'), ('JavaScript');

-- ADDING TECHNOLOGIES RELATED TO SPECIFIC LANGUAGES

INSERT INTO technologies (name, language_id) VALUES ('Flask', 1), ('Django', 1), ('ASP.NET Core', 2), ('Angular', 3), ('Express', 3);

-- ADDING OTHER TECHNOLOGIES USED

INSERT INTO technologies (name) VALUES ('MySQL'), ('SQLite'), ('MongoDB'), ('Mongoose');

-- ADDING A FEW STACKS

INSERT INTO monthly_stacks (start_date, end_date, language_id) VALUES ('2018-11-23','2018-12-21', 1), ('2018-12-21','2019-2-1', 1);

-- ADDING ERRORS

-- PYTHON
INSERT INTO error_messages (message, display_name, language_id) VALUES ('AttributeError', 'Attribute', 1), ('ImproperlyConfiguredError', 'ImproperlyConfigured', 1), ('TemplateSyntaxError', 'TemplateSyntax', 1), ('ModuleNotFoundError', 'ModuleNotFound', 1), ('ValueError', 'Value', 1), ('KeyError', 'Key', 1), ('ImportError', 'Import', 1), ('SyntaxError', 'Syntax', 1), ('BadRequestKeyError', 'BadRequestKey', 1), ('RuntimeError', 'Runtime', 1), ('UnboundLocalError', 'UnboundLocal', 1), ('Method Not Allowed', 'Method Not Allowed', 1), ('NameError', 'Name', 1), ('Template Not Found', 'Template Not Found', 1), ('TypeError', 'Type', 1), ('socket.error', 'Socket', 1), ('IndexError', 'Index', 1), ('MultiValueDictKeyError', 'MultiValueDictKey', 1);