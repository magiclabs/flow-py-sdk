.PHONY: generate
generate:
	poetry run python -m grpc_tools.protoc --python_betterproto2_out=src/magic_flow/proto -I ./proto ./proto/flow/**/*.proto
