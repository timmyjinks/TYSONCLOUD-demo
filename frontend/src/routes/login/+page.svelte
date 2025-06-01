<script lang="ts">
	import { enhance } from '$app/forms';
	export let form;
</script>

<div class="flex min-h-screen items-center justify-center px-4 text-white">
	<div class="w-full max-w-lg rounded-lg bg-gray-800 p-8 shadow-lg">
		<h1 class="mb-6 text-center text-3xl font-bold">
			TYSONCLOUD<span
				style="border-radius: 1000px; color: var(--color-indigo-400); border: 2px solid
              var(--color-indigo-400); padding: 0 8px; margin-left: 10px"
				>demo
			</span>
			<br />
			Login
		</h1>
		<form action="?/login" use:enhance method="post" class="space-y-4">
			<div>
				<label for="username" class="block text-sm font-medium">Username</label>
				<input
					type="text"
					id="username"
					name="username"
					required
					class="w-full rounded-md border border-gray-600 bg-gray-700 px-4 py-2 text-gray-400 transition focus:ring-2 focus:ring-indigo-500 focus:outline-none"
					placeholder="Enter your username"
				/>
			</div>
			<div>
				<label for="password" class="block text-sm font-medium">Password</label>
				<input
					type="password"
					id="password"
					name="password"
					required
					class="w-full rounded-md border border-gray-600 bg-gray-700 px-4 py-2 text-gray-400 transition focus:ring-2 focus:ring-indigo-500 focus:outline-none"
					placeholder="Enter your password"
				/>
			</div>
			{#if form?.error}
				<p class="rounded-md bg-red-500 p-[8px]">{form?.error}</p>
			{/if}
			<button
				type="submit"
				class="w-full rounded-md bg-indigo-600 py-2 font-semibold transition duration-200 hover:bg-indigo-700"
			>
				Log In
			</button>
		</form>
		<p class="mt-4 text-center text-sm">
			Don't have an account? <a href="/signup" class="text-indigo-400 hover:underline">Sign Up</a>
		</p>
	</div>
</div>
