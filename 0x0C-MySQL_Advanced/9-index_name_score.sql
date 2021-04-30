-- index name score
-- create index in table names
CREATE INDEX idx_name_first_score ON names (name(1), score);