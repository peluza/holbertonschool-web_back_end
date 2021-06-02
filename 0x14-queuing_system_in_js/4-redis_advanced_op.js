#!/usr/bin/node
import redis from 'redis';
import { promisify } from 'util';

const cli = redis.createClient();
const addAsync = promisify(cli.get).bind(cli);

cli.on('error', (error) => {
    console.log(`Redis client not connected to the server: ${error.message}`);
});

cli.on('connect', () => {
    console.log('Redis client connected to the server');
});

//Node Redis client and advanced operations
const KEYHASH = 'HolbertonSchools';

let keys = ['Portland', 'Seattle', 'New York', 'Bogota', 'Cali', 'Paris'];
let values = [50, 80, 20, 20, 40, 2];

keys.forEach((key, index) => {
  cli.hset(KEYHASH, key, values[index], redis.print);
});

cli.hgetall(KEYHASH, (err, value) => {
  console.log(value);
});