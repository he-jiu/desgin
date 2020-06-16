<template>
	<view>
		<form @submit="submitInformation">
			<view class='input-group'>
				<view class='input'>
					员工号：<input name='staffID' placeholder="输入员工号" />
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
				
				if(e.detail.value.staffID==''){
					uni.showToast({
						icon:'none',
						title:'未填写员工号'
					})
				}

				else{
					console.log('form发生了submit事件，携带数据为：' + JSON.stringify(e.detail.value))
					var formdata = e.detail.value;
					uni.request({
						url:'http://182.92.239.229/deletestaff',
						data:e.detail.value,
						success: (res) => {
							console.log(res.data);
							if(res.data=='False'){
								uni.showToast({
									icon:'none',
									title:'没有此员工'
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
					// uni.showModal({
					// 	content: '表单数据内容：' + JSON.stringify(formdata),
					// 	showCancel: false,
						
					// });
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

