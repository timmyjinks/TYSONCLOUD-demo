import type { PageServerLoad } from '../sign_up/$types';
import PocketBase from 'pocketbase';
import { error, redirect, fail } from '@sveltejs/kit';
import { POCKETBASE_EMAIL, POCKETBASE_PASSWORD } from '$env/static/private';

export const load = (async ({ locals }) => {
	if (locals.pb.authStore.isValid) {
		throw redirect(303, '/');
	}
	return {
		user: locals.user
	};
}) satisfies PageServerLoad;

export const actions = {
	signup: async ({ request, locals }) => {
		const formData = await request.formData();
		const username = formData.get('username') as string;
		const password = formData.get('password') as string;
		const passwordConfirm = formData.get('passwordConfirm') as string;

		if (password != passwordConfirm) {
			return fail(422, {
				error: 'Passwords do not match'
			});
		} else if (password.length < 5) {
			return fail(422, {
				error: 'Password must be at least 5 characters'
			});
		}

		const pb = new PocketBase('https://pocketbase-test.tysonjenkins.dev');
		await pb.admins.authWithPassword(POCKETBASE_EMAIL, POCKETBASE_PASSWORD);

		try {
			await pb.collection('users').create({
				username: username,
				password: password,
				passwordConfirm: passwordConfirm
			});

			await locals.pb
				.collection('users')
				.authWithPassword(username.toString(), password.toString());
		} catch (err: any) {
			console.log(err);
			return fail(422, {
				error: 'User already exists'
			});
		}
		throw redirect(303, '/');
	}
};
