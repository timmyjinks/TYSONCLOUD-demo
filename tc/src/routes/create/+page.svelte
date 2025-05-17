<script lang="ts">
	export let data;
	export let form;
</script>

<div class="flex min-h-screen flex-col">
	<nav class="bg-gray-800 shadow-lg">
		<div class="mx-auto max-w-7xl px-4 sm:px-6 lg:px-8">
			<div class="flex h-16 justify-between">
				<div class="flex items-center">
					<a href="/dashboard" class="text-2xl font-bold text-indigo-400"
						>TYSONCLOUD <span
							style="border-radius: 1000px; color: var(--color-indigo-400); border: 2px solid
              var(--color-indigo-400); padding: 0 8px; margin-left: 10px"
							>demo
						</span>
					</a>
				</div>
				<div class="flex items-center">
					<button
						on:click
						class="rounded-md bg-indigo-600 px-4 py-2 text-sm font-semibold text-white transition duration-200 hover:bg-indigo-700"
					>
						Log Out
					</button>
				</div>
			</div>
		</div>
	</nav>
	<div class="flex flex-1 items-center justify-center px-4 py-8 text-white">
		<div class="w-full max-w-md rounded-lg bg-gray-800 p-8 shadow-lg">
			<h1 class="mb-6 text-center text-3xl font-bold">Create Database</h1>
			<form action="?/create" method="post" class="space-y-4">
				<div>
					<label for="db-name" class="block text-sm font-medium">Database Name</label>
					<input
						type="text"
						id="db-name"
						name="database_name"
						required
						class="w-full rounded-md border border-gray-600 bg-gray-700 px-4 py-2 text-gray-400 transition focus:ring-2 focus:ring-indigo-500 focus:outline-none"
						placeholder="Enter database name"
					/>
				</div>
				<div>
					<label for="pg-username" class="block text-sm font-medium">PostgreSQL Username</label>
					<input
						type="text"
						id="pg-username"
						name="database_username"
						required
						class="w-full rounded-md border border-gray-600 bg-gray-700 px-4 py-2 text-gray-400 transition focus:ring-2 focus:ring-indigo-500 focus:outline-none"
						placeholder="Enter PostgreSQL username"
					/>
				</div>
				<div>
					<label for="pg-password" class="block text-sm font-medium">PostgreSQL Password</label>
					<input
						type="password"
						id="pg-password"
						name="database_password"
						required
						class="w-full rounded-md border border-gray-600 bg-gray-700 px-4 py-2 text-gray-400 transition focus:ring-2 focus:ring-indigo-500 focus:outline-none"
						placeholder="Enter PostgreSQL password"
					/>
				</div>
				<button
					type="submit"
					class="w-full rounded-md bg-indigo-600 py-2 font-semibold transition duration-200 hover:bg-indigo-700"
				>
					Create Database
				</button>
			</form>
			<p class="mt-4 text-center text-sm">
				<a href="/" class="text-indigo-400 hover:underline">Back to Dashboard</a>
			</p>
		</div>
	</div>
</div>
