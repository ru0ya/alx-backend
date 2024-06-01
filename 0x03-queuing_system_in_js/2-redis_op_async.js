import redis from 'redis';
const client = redis.createClient();
const { promisify } = require('util');


redisClient.on('ready', () => {
	console.log('Redis client connected to the server');
});


redisClient.on('error', (err) => {
	console.log("Redis client not connected to the server: ERROR_MESSAGE");
});


function setNewSchool(schoolName, value) {
	client.set('schoolName', 'value', redis.print);
};


const getAsync = promisify(client.get).bind(client);


async function displaySchoolValue(schoolName) {
	try {
		const value = getAsync(schoolName);
		console.log(`${value}`);
	} catch (error) {
		console.error(error);
	}
}


displaySchoolValue('Holberton');
setNewSchool('HolbertonSanFrancisco', '100');
displaySchoolValue('HolbertonSanFrancisco');
