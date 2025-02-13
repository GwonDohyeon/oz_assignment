import {
	S3Client,
	CreateBucketCommand,
	PutObjectCommand,
} from '@aws-sdk/client-s3';

export async function main(){
	const s3Client = new S3Client({});
	const bucketName = 'dhg1221-bucket-20250210-01';
	await s3Client.send(
		new CreateBucketCommand({
			Bucket: bucketName,
		})
	);

	await s3Client.send(
		new PutObjectCommand({
			Bucket: bucketName,
			Key: 'hello.txt',
			Body: 'Hello, JavaScript SDK!',
		})
	);
}

main();
