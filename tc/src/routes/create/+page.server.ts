import type { PageServerLoad } from './$types';
import { redirect } from '@sveltejs/kit';

export const load = (async ({ locals }) => {
	return {
		user: locals.user
	};
}) satisfies PageServerLoad;

export const actions = {
	create: async ({ request, locals }) => {
		const formData = await request.formData();
		const database_name = formData.get('database_name').replace(/[^a-zA-Z0-9-_]/g, '') as string;
		const database_username = formData.get('database_username').replace(/[^a-zA-Z]/g, '') as string;
		const database_password = formData.get('database_password') as string;
		const username = locals.user?.username;
		console.log(username);

		const response = await fetch('http://dockerapi:8000/database', {
			method: 'POST',
			headers: { 'Content-Type': 'application/json' },
			body: JSON.stringify({
				username: username,
				database_name: database_name,
				database_username: database_username,
				database_password: database_password
			})
		});

		throw redirect(303, '/');
	}
};
