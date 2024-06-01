import redis from 'redis';
const client = redis.createClient();


redisClient.on('ready', () => {
	console.log('Redis client connected to the server');
});


redisClient.on('error', (err) => {
	console.log("Redis client not connected to the server: ERROR_MESSAGE");
});
