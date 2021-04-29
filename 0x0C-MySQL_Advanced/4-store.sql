-- store
-- creates a trigger that decreases 
CREATE TRIGGER orderdata
BEFORE INSERT ON orders
FOR EACH ROW UPDATE items SET quantity = quantity - NEW.number WHERE name = NEW.item_name;