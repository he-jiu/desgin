<template>
	<view>
		<form @submit="submitInformation">
			<view class='input-group'>
				<view class='input'>
					用户编号：<input name='userID' placeholder="输入用户编号" />
				</view>
	
			</view>
			<view>
				<button form-type="submit" type="warn">删除</button>
			</view>
		</form>
	</view>
</template>

<script>
	export default{
		data(){
			return{
				
			}
		},
		methods:{

			submitInformation:function(e){
				
				if(e.detail.value.userID==''){
					uni.showToast({
						icon:'none',
						title:'未填写用户编号'
					})
				}

				else{
					console.log('form发生了submit事件，携带数据为：' + JSON.stringify(e.detail.value))
					var formdata = e.detail.value;
					uni.request({
						url:'http://182.92.239.229/deleteusers',
						data:e.detail.value,
						success: (res) => {
							console.log(res.data);
							if(res.data=='False'){
								uni.showToast({
									icon:'none',
									title:'没有该用户'
								})
							}
							else{
								uni.showToast({
									icon:'none',
									title:'删除成功'
								});
								setTimeout(function(){uni.navigateBack()},1000);
							}
						}
					})
				}
			}
		}
	}
</script>

<style>
	.input{
		display: flex;
		margin: 30rpx;
		border-bottom: solid 1rpx #C8C7CC;
		
	}
	.picker{
		display: flex;
		margin: 30rpx;
		border-bottom: solid 1rpx #C8C7CC;
		
	}
</style>

