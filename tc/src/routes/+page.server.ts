import type { PageServerLoad } from './$types';
import { redirect } from '@sveltejs/kit';

export const load = (async ({ locals }) => {
	if (!locals.pb.authStore.isValid) {
		throw redirect(303, '/login');
	}

	const response = await fetch('http://dockerapi:8080/databases', {
		method: 'POST',
		headers: { 'Content-Type': 'application/json' }
		// body: JSON.stringify([])
	});

	const data = await response.json();

	return {
		databases: data,
		user: locals.user
	};
}) satisfies PageServerLoad;

export const actions = {
	logout: async ({ locals }) => {
		locals.pb.authStore.clear();
		locals.user = null;

		redirect(303, '/login');
	}
};
