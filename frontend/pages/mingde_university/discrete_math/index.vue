<template>
  <div style="margin:auto;width:70%">
    <h2>離散数学（準備中）</h2>
    <el-button 
      @click="drawer = true" 
      type="primary" 
      style="margin-left:30px">
      メモ
    </el-button>
    <div>
      <el-tree :data="data" :props="defaultProps" @node-click="handleNodeClink"></el-tree>
    </div>
    <el-drawer
      :with-header="false"
      title="タイトル"
      :visible.sync="drawer"
      :direction="direction"
      size="75%"
      >
      <div class="drawer_content">
        <h1>メモ</h1>
      </div>
      <div>
        <el-button type="primary" @click="innerDrawer = true" id="write-b">書き</el-button>
        <el-drawer
          :append-to-body="true"
          direction ="ltr"
          size="50%"
          :before-close="handleClose"
          :with-header="false"
          :visible.sync="innerDrawer"
          custom-class="demo-drawer"
          ref="innerDrawer">
          <div class="drawer_content">
            <h1>メモ</h1>
            <el-form  :model="form" class="drawer_content">
              <el-form-item label="主题" :label-width="formLabelWidth">
                <el-input
                v-model="form.theme"
                autocomplete="off">
              </el-input>
              </el-form-item>
              <el-form-item label="内容" :label-width="formLabelWidth">
                <el-input  
                  type="textarea" 
                  v-model="form.content" 
                  autocomplete="off"  
                  :autosize="{ minRows: 10, maxRows: 14}">
                </el-input>
              </el-form-item>
            </el-form>
            <div class="drawer_footer">
              <el-button @click="$refs.innerDrawer.closeDrawer()">取 消</el-button>
              <el-button type="primary" @click="$refs.innerDrawer.closeDrawer()">确 定</el-button>
            </div>
          </div> 
        </el-drawer>
      </div>
    </el-drawer>
  </div>
</template>
<script>
export default {
  data () {
    return {
      data: [{
        label: '１、集合',
        children: [{
          label: '集合定義と演算',
          children: [{
            label: '集合定義'
          }]
        },
        {
          label: '写像とその合成'
        },
        {
          label: '代数系',
          children:[{
            label:'半群・群',
           
          },
          {label:'環・体'},]
        }
        ]
      }, {
        label: '２、命題倫理と述語倫理',
        children: [{
          label: '複合命題',
          children: [{
            label: '命題計算'
          }]
        }, 
        {
          label: '含意と推論',
        },
        {
          label: '述語倫理',
        }]
      }, 
      {
        label: '３、ブール代数',
        children: [{
          label: 'ブール代数定義',
        }, {
          label: 'ブール論理式',
        }]
      }, {
        label: '４、行列と行列式',
        children: [{
          label: '行列',
        }, {
          label: '行列式',
        },
        {
          label: '行列式の性質',
        },
        {
          label: '余因子行列と逆行列',
        },
        {
          label: '連立一次方程式',
        },
      ]
      },
      {
        label: '５、関係',
        children: [{
          label: '二項関係',
        }, 
        {
          label: '同値関係',
        },
        {
          label: '順序関係と束',
        }]
      },
      {
        label: '６、グラフ理論',
        children: [{
          label: '基礎概念',
        }, 
        {
          label: '名前のついたグラフ',
        },
        {
          label: '用いたグラフ表現',
        },
        {
          label: '平面グラフと非平面グラフ',
        },
        {
          label: '木，根付き木，順序根付き木',
        }]
      },
      {
        label: '７、組合せ解析',
        children: [{
          label: '場合の数',
        }, 
        {
          label: '順列',
        },
        {
          label: '組合せ',
        },
        {
          label: '多項定理',
        }]
      },
    ],
    form:{
          theme :'',
          content: ''
        },
    formLabelWidth:'80px',
    timer:null,
    drawer:false,
    innerDrawer:false,
    dialog:false,
    direction:'ltr',
      defaultProps: {
        children: 'children',
        label: 'label'
      }
    }
  },
  method:{
      handleClose(done) {
      if (this.loading) {
        return;
      }
    },
      cancelForm() {
      this.loading = false;
      this.dialog = false;
      clearTimeout(this.timer);
    }
    }
}
</script>