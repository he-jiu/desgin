<template>
	<view>
		<form @submit="submitInformation">
			<view class='input-group'>
				<view class='input'>
					员工号：<input name='staffID' placeholder="输入员工号" />
				</view>
				<view class='picker'>
					员工种类：<picker @change="staffKind" name='staffKind' :value="staffKindIndex" :range="staffKindArray" >{{staffKindArray[staffKindIndex]}}</picker>
				</view>
				<view class='input'>
					电话号码：<input name='telephone' placeholder="输入电话号码" />
				</view>
			</view>
			<view>
				<button form-type="submit" type="primary">提交</button>
			</view>
		</form>
	</view>
</template>

<script>
	var  r=/^1[3|4|5|8][0-9]\d{4,8}$/;
	export default{
		data(){
			return{
				staffKindIndex:0,
				staffKindArray:[
					'请选择员工种类(01为操作员，02为管理员)','01','02'
				]
			}
		},
		methods:{
			staffKind:function(e){
				this.staffKindIndex=e.target.value;
			},
			submitInformation:function(e){
				
				if(e.detail.value.staffID==''){
					uni.showToast({
						icon:'none',
						title:'未填写员工号'
					})
				}
				else if(e.detail.value.staffKind==0){
					uni.showToast({
						icon:'none',
						title:'还未选择员工种类'
					})
				}
				else if(!r.test(e.detail.value.telephone)){
					uni.showToast({
						icon:'none',
						title:'手机号不合法'
					})
				}

				else{
					e.detail.value.staffKind=this.staffKindIndex;
					console.log('form发生了submit事件，携带数据为：' + JSON.stringify(e.detail.value))
					var formdata = e.detail.value;
					uni.request({
						url:'http://182.92.239.229/changestaffmessage',
						data:e.detail.value,
						success: (res) => {
							if(res.data=='True'){
								uni.showToast({
									icon:'none',
									title:'修改成功'
								});
								setTimeout(function(){uni.navigateBack()},1000)
							}
							else{
								uni.showToast({
									icon:'none',
									title:'修改失败'
								});
								
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

