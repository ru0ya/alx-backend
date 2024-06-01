import redis from 'redis';
const client = redis.createClient();


redisClient.on('ready', () => {
	console.log('Redis client connected to the server');
});


redisClient.on('error', (err) => {
	console.log("Redis client not connected to the server: ERROR_MESSAGE");
});


function setNewSchool(schoolName, value) {
	client.set('schoolName', 'value', redis.print);
};


function displaySchoolValue(schoolName) {
	client.get(schoolName, function(error, value) {
		if (error) {
			console.error(error);
		} else {
			console.log(`${value}`);
		}
	});
}


displaySchoolValue('Holberton');
setNewSchool('HolbertonSanFrancisco', '100');
displaySchoolValue('HolbertonSanFrancisco');
