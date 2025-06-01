FROM oven/bun AS builder
WORKDIR /app
COPY . .
RUN bun i
RUN bun run build

FROM oven/bun
COPY --from=builder /app/build .

ENV ORIGIN=https://tysoncloud-demo.tysonjenkins.dev
ENV PROTOCOL_HEADER=x-forwarded-proto
ENV HOST_HEADER=x-forwarded-host

EXPOSE 3000
CMD ["bun", "run", "start"]
