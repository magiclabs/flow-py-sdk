.PHONY: generate
generate:
	poetry run python -m grpc_tools.protoc --python_betterproto_out=magic_flow_python/proto -I ./proto ./proto/flow/**/*.proto
