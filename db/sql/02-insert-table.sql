DELIMITER $$

CREATE TRIGGER `beverage`.tr_ins_after
    AFTER INSERT
    ON `beverage`.pop FOR EACH ROW
BEGIN
    INSERT INTO `test_chained`.pop (id, name, color) VALUES(new.id, new.name, new.color);
    INSERT INTO `test_raw`.pop (id, name, color) VALUES(new.id, new.name, new.color);
    INSERT INTO `test_api`.pop (id, name, color) VALUES(new.id, new.name, new.color);
END$$    

DELIMITER ;

TRUNCATE `beverage`.pop;
TRUNCATE `test_chained`.pop;
TRUNCATE `test_raw`.pop;
TRUNCATE `test_api`.pop;

INSERT INTO `beverage`.pop (id, name, color)
VALUES
(default, 'RC Cola', 'brown'),
(default, 'Sprite', 'clear'),
(default, 'Verners', 'brown'),
(default, 'Mt. Lightening', 'green');

DROP TRIGGER `beverage`.tr_ins_after;